import itchatmp
import cy
import random_num
import qianming

itchatmp.update_config(itchatmp.WechatConfig(
    token='your token',
    appId='your appId',
    appSecret='your appSecret'))

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    if msg['Content'] == '帮助':
        return '帮助信息'
    
    elif re.search('[0-9]', msg['Content'][0]) and re.search('(-)', msg['Content'][:]) and re.search('[0-9]', msg['Content'][-1]):
        num = msg.split('-')
        return str(random_num.random_number(int(num[0]), int(num[-1])))
    
    elif msg['Content'][0] in ['q', 'Q'] and len(msg['Content']) > 1:
        return qianming.qm(msg['Content'][1:])
    
    else:
        key = msg['Content'][-1]
        if "\u4e00" <= key <= "\u9fa5":
            return cy.cy(key)
        else:
            return '最后一个字须为汉字，且末尾不能有空格'

@itchatmp.msg_register(itchatmp.content.EVENT)
def user_management(event):
    if event['Event'] == 'subscribe':
        return u'终于等到你！\n回复「帮助」获取更多信息'
