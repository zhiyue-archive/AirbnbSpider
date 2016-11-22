# AirbnbSpider
a spider crawl all room info of airbnb ,include reservation of the rooms

##AirbnbBeijingSpider
the key point of spider is the url 'https://zh.airbnb.com/search/search_results?location={}'. If you just put 'beijing' or '北京', it only returns no only 300 rooms. So you have to spilt the address to some more small districts such as '北京团结湖','北京王府井'.But there is a little trick here,if you put '奥林匹克公园' instead of '北京市朝阳区大屯路奥林匹克公园（西北门）', it may return some results all over the world not the rooms near '奥林匹克公园' of beijing.So you have to put every address above with the url in chrome or firefox , and test the results.

##Proxy or Tor
You should set some time sleep or a proxy to prevent banning by airbnb.Here I set up the tor according to the tutorial 'http://pkmishra.github.io/blog/2013/03/18/how-to-run-scrapy-with-TOR-and-multiple-browser-agents-part-1-mac'.Great tutorial. But unfortunately you can't access the home page of tor project , so you couln't just install tor by 'apt-get install tor'.Compiling the source code maybe a better way or renting a host out of china.

##airbnb_beijing_cal
If you don't know any knowledge about website or frontend you won't find the url. You could get every home's infomation about available or not in the last three months.The items that returns have two values,true or false.True meanings the room is available or not rent out in that day. But the host could set the value to false manually ,and actually the room wasn't rent out .So you have to develop some algorithm to detect it.

listing_id is the home id in the crawled result above . You have to run the spider above first and then this.


