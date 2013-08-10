#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from google.appengine.api import users
import urllib2
import urllib
import json
#from google.appengine.api import urlfetch
#urlfetch.set_default_fetch_deadline(60) 

MAIN_PAGE_HTML = """\
<!DOCTYPE html>
<html>
<head lang="ja">
  <title>白ヤギが要約します</title>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/kube.css" />
  <link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/master.css" />

  <script type="text/javascript" src="http://code.jquery.com/jquery.min.js"></script>

  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->

</head>
<body>
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ja_JP/all.js#xfbml=1&appId=592495467469246";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>


<div id="page">
<header id="header" class="clearfix">
  <div class="conatainer clearfix">
      <h1 id="logo">シロサム</h1>
        <div id="social-btns">
          <div id="twitter"><a href="https://twitter.com/share" class="twitter-share-button" data-url="http://shirosum.appspot.com/" data-text="シロサムでテキストを自動要約" data-lang="ja" data-hashtags="shirosum">ツイート</a>
      <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script></div>
          <div id="facebook"><div class="fb-like" data-width="450" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="false" data-send="false"></div></div><!-- / #facebook -->
      </div>
    </div>
</header>

<div id="section-desc">
  <h1 id="h-desc" class="text-shadow clear">テキストを自動で要約します</h1>
  <p id="desc">このサービスはごくシンプルなルールに基づいてテキストの自動要約を行います。与えられた文章の中から最も重要な3つのポイントを抜き出すことで、限られた時間の中でも効率よく情報を吸収できることを目的にしています。要約したいサイトのURLを入力するか、タイトルと本文をコピペしてご利用ください</p>
</div>

<div>
<form method="post" action="/sign" class="forms">

  <div id="section-1" class="section">
    <h1>①URLで要約</h1>
  <label>
    URL
    <table class="width-100 table-flat">
      <tr>
        <td><span class="input-prepend">http://</span></td>
        <td class="width-100"><input type="url" name="url" class="width-100"></td>
      </tr>
    </table>
  </label>  
    <p class="text-centered"><input type="submit" class="btn" value="要約"></p>
    </div>  
    
    <div id="section-2" class="section">
    <h1>②コピペで要約</h1>
    <label>
    タイトル
    <input type="text" name="title" size="100" />
  </label>
    
  <label>
    本文
    <textarea name="body" rows="5" class="width-100"></textarea>
  </label>
    </div>

  <p class="text-centered"><input type="submit" class="btn" value="要約"></p>
</form>
</div>
</div><!-- / #page -->
<footer>
    <div class="logo">
      <img src="https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn1/1011356_472146862874199_299690691_n.jpg" width="400pt">
    </div>
    <ul id="footer-list">
      <li><a href="http://shiroyagi.co.jp/" target="_blank">会社概要</a></li>
        <li><a href="https://www.wantedly.com/companies/shiroyagi/" target="_blank">メンバー募集中</a></li>
        <li><a href="https://www.facebook.com/shiroyagico/" target="_blank">Facebookページ</a></li>
        <li><a href="http://aial.shiroyagi.co.jp/">最先端情報吸収研究所</a></li>
    </ul> 
</footer>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
      def post(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        checkbox=None
        if cgi.escape(self.request.get('evaluation')): checkbox=int(cgi.escape(self.request.get('evaluation')))
        
        if checkbox:
          data={}
          data['id']='shirosum_evaluate'
          data['checkbox']=checkbox
          url=u'http://mixtape.jp/'
          req = urllib2.Request(url, headers=headers, data=json.dumps(data))
          response=urllib2.urlopen(req)
          html = response.read()
          self.response.write('''
<!DOCTYPE html>
<html lang="ja">
<head>
	<title>白ヤギが要約しました</title>

	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/kube.css" />
	<link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/master.css" />

	<script type="text/javascript" src="http://code.jquery.com/jquery.min.js"></script>
    <script type="text/javascript" src="http://shiroyagi.co.jp/shirosum/js/html5shiv.js"></script>
	<script type="text/javascript" src="http://shiroyagi.co.jp/shirosum/js/respond.min.js"></script>

	<!--[if lt IE 9]>
	<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->

</head>
<body>

<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ja_JP/all.js#xfbml=1&appId=592495467469246";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

<div id="page">
<header id="header" class="clearfix">
	<div class="conatainer clearfix">
    	<h1 id="logo">シロサム</h1>
        <div id="social-btns">
        	<div id="twitter"><a href="https://twitter.com/share" class="twitter-share-button" data-url="http://shirosum.appspot.com/" data-text="シロサムでテキストを自動要約" data-lang="ja" data-hashtags="shirosum">ツイート</a>
			<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script></div>
        	<div id="facebook"><div class="fb-like" data-width="450" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="false" data-send="false"></div></div><!-- / #facebook -->
    	</div>
    </div>
</header>

<div id="section-desc">
	<h1 id="h-desc" class="text-shadow clear">ご協力ありがとうございました。</h1>
	<p id="desc">これからも白ヤギをよろしくお願いします！</p>
</div>

<h1 class="medium blue"></h1>
<div id="section-2-done" class="section">
<h2 class="article-title text-shadow">白ヤギはニュースリーディングの新しいスタンダードに</h2>
    <p>
      しろヤギコーポレーションでは自動要約を始めとする多数の先端研究に基づき、ビジネスパーソンのための新しいニュースサービスを開発中です。
      近日中にテストローンチを予定しておりますので、ご興味のある方は下記よりご登録下さい。
    </p>
</div>

<p><a href="http://shirosum.appspot.com/">もう一度要約する</a></p>       
</div><!-- / #page -->
<footer>
    <div class="logo">
    	<img src="https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn1/1011356_472146862874199_299690691_n.jpg" width="400pt">
    </div>
    <ul id="footer-list">
    	<li><a href="http://shiroyagi.co.jp/" target="_blank">会社概要</a></li>
        <li><a href="https://www.wantedly.com/companies/shiroyagi/" target="_blank">メンバー募集中</a></li>
        <li><a href="https://www.facebook.com/shiroyagico/" target="_blank">Facebookページ</a></li>
        <li><a href="http://aial.shiroyagi.co.jp/">最先端情報吸収研究所</a></li>
    </ul>	
</footer>
</body>
</html>
''')
        else:
          print 'else'
          title=cgi.escape(self.request.get('title'))
          body=cgi.escape(self.request.get('body'))
          url=cgi.escape(self.request.get('url'))

          data={}
          data['id']='shirosum_post'
          data['title']=title.encode("utf-8")
          data['body']=body.encode("utf-8")
          data['url']=url.encode("utf-8")
          url=u'http://mixtape.jp/'
          req = urllib2.Request(url, headers=headers, data=json.dumps(data))
          response=urllib2.urlopen(req)
          html = response.read()
          jres=json.loads(html)

          self.response.write('''
<!DOCTYPE html>
<html lang="ja">
<head>
	<title>白ヤギが要約しました</title>

	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/kube.css" />
	<link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/master.css" />

	<script type="text/javascript" src="http://code.jquery.com/jquery.min.js"></script>
    <script type="text/javascript" src="http://shiroyagi.co.jp/shirosum/js/html5shiv.js"></script>
	<script type="text/javascript" src="http://shiroyagi.co.jp/shirosum/js/respond.min.js"></script>

	<!--[if lt IE 9]>
	<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->

</head>
<body>

<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ja_JP/all.js#xfbml=1&appId=592495467469246";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

<div id="page">
<header id="header" class="clearfix">
	<div class="conatainer clearfix">
    	<h1 id="logo">シロサム</h1>
        <div id="social-btns">
        	<div id="twitter"><a href="https://twitter.com/share" class="twitter-share-button" data-url="http://shirosum.appspot.com/" data-text="シロサムでテキストを自動要約" data-lang="ja" data-hashtags="shirosum">ツイート</a>
			<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script></div>
        	<div id="facebook"><div class="fb-like" data-width="450" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="false" data-send="false"></div></div><!-- / #facebook -->
    	</div>
    </div>
</header>

<div id="section-desc">
	<h1 id="h-desc" class="text-shadow clear">要約完了 (要約率''')

          self.response.write(jres['compression'])
          self.response.write('''%)</h1>
	<p id="desc">戦略コンサル風に言うと「この文章のポイントは３つあって・・・」要約終了しました。<br>よろしければどれくらい正確な要約になっているか評価をおねがいします。評価をいただくごとに機械学習アルゴリズムが賢くなっていきますので、今後のサービスの向上にリアルに効果があります。ご利用ありがとうございました！</p>
</div>

<h1 class="medium blue"></h1>
<div id="section-2-done" class="section">
	
''')
          if jres.has_key('title'):
            self.response.write('<h2 class="article-title text-shadow">'+jres['title']+'</h2>')
          else:
            self.response.write('<h2 class="article-title text-shadow">タイトルが見つかりませんでした</h2>')
          self.response.write('''

    <p>1.
    ''')
          if len(jres['bullets'])>0:
            self.response.write(jres['bullets'][0][0])
          self.response.write('''
    </p>
    <p>2.
    ''')
          if len(jres['bullets'])>1:
            self.response.write(jres['bullets'][1][0])
          self.response.write('''
    </p>
    <p>3.
    ''')
          if len(jres['bullets'])>2:
            self.response.write(jres['bullets'][2][0])
          self.response.write('''
</p>
</div>

<div id="section-3" class="section">
	<p>
    	<form method="post" action="/sign" class="forms">
		<label><h3>アルゴリズムの向上のため評価をお願いします <em class="req">*</em></h3></label>
		<ul class="forms-inline-list">
			<li><input name="evaluation" value="1" type="radio"> <label>非常に良い</label></li>
			<li><input name="evaluation" value="2" type="radio"> <label>良い</label></li>
			<li><input name="evaluation" value="3" type="radio"> <label>普通</label></li>
			<li><input name="evaluation" value="4" type="radio"> <label>悪い</label></li>
      <li><input name="evaluation" value="5" type="radio"> <label>非常に悪い</label></li>
		</ul>
        <input type="submit" class="btn" value="送信">
        </form>
	</p>
</div>
 
</div><!-- / #page -->
<footer>
    <div class="logo">
    	<img src="https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn1/1011356_472146862874199_299690691_n.jpg" width="400pt">
    </div>
    <ul id="footer-list">
    	<li><a href="http://shiroyagi.co.jp/" target="_blank">会社概要</a></li>
        <li><a href="https://www.wantedly.com/companies/shiroyagi/" target="_blank">メンバー募集中</a></li>
        <li><a href="https://www.facebook.com/shiroyagico/" target="_blank">Facebookページ</a></li>
        <li><a href="http://aial.shiroyagi.co.jp/">最先端情報吸収研究所</a></li>
    </ul>	
</footer>



</body>
</html>
''')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', Guestbook),
    ], debug=True)

