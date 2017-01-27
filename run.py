import syspider
import qqapi

qq = qqapi.Sender("http://swz1994.com:5000")

news = syspider.check_news()
news2 = syspider.check_news2()

if news != False:
	qq.send_message(614291728, news, "group")
	qq.send_message(323294261, news, "group")
	qq.send_message(466920269, news, "group")
if news2 != False:
	qq.send_message(614291728, news2, "group")
	qq.send_message(323294261, news2, "group")
	qq.send_message(466920269, news2, "group")