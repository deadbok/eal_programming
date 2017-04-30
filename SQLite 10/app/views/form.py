'''
@since: 13 Aug 2016
@author: oblivion
'''
from datetime import datetime, timedelta
from flask import abort
from flask import current_app
from flask import render_template
from flask import request
from flask.views import MethodView
import smtplib
from socket import getfqdn

import app
from app.pcomment import PostedComment


class Form(MethodView):
    '''
    View to show the comment form.
    '''
    # Only support GET and POST requests.
    methods = ['GET', 'POST']

    def __init__(self):
        '''
        Constructor
        '''
        self.nonce = None

    def send_mod_email(self, from_addr, to_addr_list, cc_addr_list=[],
                       subject='', message=''):
        '''
        Send en email to the moderator about the post.

        @todo: Error handling.
        '''
        header = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(current_app.config['SMTP_SERVER'],
                              current_app.config['SMTP_PORT'])
        server.starttls()
        server.login(current_app.config['SMTP_LOGIN'],
                     current_app.config['SMTP_PASSWD'])
        problems = server.sendmail(from_addr, to_addr_list, message)

        server.quit()

    def get(self, post):
        '''
        Render the comment form.
        '''
        # Create a secret for the form
        self.nonce = app.FORM_NONCES.new(ntype=app.FORM_TYPE)
        app.save_json()

        current_app.logger.debug("Rendering comment form template.")
        return render_template('add.html', nonce=self.nonce, post=post,
                               tid=request.args.get('tid', 0),
                               subject=request.args.get('subject', ''),
                               url='http://' + getfqdn() + ':5000/post/')

    def post(self):
        '''
        Handle posting of comments.
        '''
        current_app.logger.info("Processing posted comment.")
        nonce = request.form['nonce']
        current_app.logger.info("Nonce: " + nonce)

        if not app.FORM_NONCES.is_active(nonce):
            current_app.logger.warning('Invalid nonce: ' + nonce)
            abort(404)

        current_app.logger.debug('Comment validated for moderation.')

        app.FORM_NONCES.free(nonce)

        comment = PostedComment(name=request.form['name'],
                                email=request.form['email'],
                                date=datetime.now(),
                                message=request.form['comment'],
                                ip=request.remote_addr)
        cnonce = app.COMMIT_NONCES.new(value=comment,
                                       timeout=datetime.now() +
                                       timedelta(days=31),
                                       ntype=app.COMMIT_TYPE)

        self.send_mod_email(from_addr=current_app.config['FROM_EMAIL'],
                            to_addr_list=[current_app.config['TO_EMAIL']],
                            subject='New comment: ',
                            message=('Name: ' + comment.name +
                                     '\nE-mail: ' + comment.email +
                                     '\nMessage:\n\n' + comment.message +
                                     '\n\nCommit link: ' + getfqdn() +
                                     ':5000/post/commit/' + cnonce
                                     )
                            )

        app.save_json()
        return "Comment recieved."
