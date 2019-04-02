#!/usr/local/pyenv/shims/python
# coding:utf-8

from slackclient import SlackClient
import AppConf

class SlackInvite:
    botIdStr = '<@' + AppConf.BOT_ID + '>'
    sc = SlackClient(AppConf.botToken)

    def __init__(self):
        if SlackInvite.sc.rtm_connect():
            # print(SlackInvite.sc.user)
            # print(SlackInvite.sc.server.login_data['self']['id'])
            
            while True:
                data = SlackInvite.sc.rtm_read()

                if(len(data) > 0) :
                    # print(data)
                    user, channel = self.slackOutputStr(data)
                    if user and channel:
                        # print(user + ", " + channel)
                        print(SlackInvite.sc.api_call("channels.invite", token=AppConf.accessToken, channel=channel, user=user))

    def slackOutputStr(self, message):
        messageList = message

        if messageList and len(messageList) > 0:
            for msg in messageList:
                if msg and 'subtype' in msg and msg['subtype'] == 'channel_leave':
                    return msg['user'], msg['channel']
        
        return None, None

cmd = SlackInvite()