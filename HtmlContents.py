#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HtmlContents(object):
  def __init__(self):
    pass

  def top_page(self, top_message):
    return self.header('白ヤギが要約します')+self.top_page_body(top_message)+self.footer()

  def summary_done_page(self, result):
    return self.header('白ヤギが要約しました')+self.summary_done_page_body(result)+self.footer()

  def thanks_page(self):
    return self.header('白ヤギが要約しました')+self.thanks_body()+self.footer()

  def header(self,title):
    return """
    <!DOCTYPE html>
    <html>
    <head lang="ja">
      <title>"""+title+"""</title>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/kube.css" />
      <link rel="stylesheet" type="text/css" href="http://shiroyagi.co.jp/shirosum/css/master.css" />

      <script type="text/javascript" src="http://code.jquery.com/jquery.min.js"></script>

      <!--[if lt IE 9]>
      <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
      <![endif]-->

    </head>
    """

  def top_page_body(self, top_message):
    text="""
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
        	<div id="facebook"><div class="fb-like" data-width="110" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="false" data-send="false"></div></div><!-- / #facebook -->
            <a href="http://b.hatena.ne.jp/entry/http://shirosum.appspot.com/" class="hatena-bookmark-button" data-hatena-bookmark-title="白ヤギが自動で要約します" data-hatena-bookmark-layout="standard-balloon" data-hatena-bookmark-lang="ja" title="このエントリーをはてなブックマークに追加"><img src="http://b.st-hatena.com/images/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a><script type="text/javascript" src="http://b.st-hatena.com/js/bookmark_button.js" charset="utf-8" async></script>
    	    </div>
        </div>
    </header>

    <div id="section-desc">
      <h1 id="h-desc" class="text-shadow clear">"""+top_message+"""</h1>
      <p id="desc">このサービスはごくシンプルなルールに基づいてテキストの自動要約を行う実験的サービスです。与えられたニュース記事の中から最も重要な3つのポイントを抜き出すことで、限られた時間の中でも効率よく情報を吸収できることを目的にしています。なお、商用利用をご希望の方は、白ヤギコーポレーション（info at shiroyagi.co.jp) までお問い合わせ下さい。なお、現在のところ英語のサイトには対応しておりませんので、ご了承下さい。</p>
    </div>

    <div>
    <form method="post" action="/sign" class="forms">

      <div id="section-1" class="section">
        <h1>1.URLで要約</h1>
      <label>
        <table class="width-100 table-flat">
          <tr>
            <td><span class="input-prepend">URL</span></td>
            <td class="width-100"><input type="url" name="url" class="width-100"></td>
          </tr>
        </table>
      </label>  
        <p class="text-centered"><input type="submit" class="btn" value="要約"></p>
        </div>  
        
        <div id="section-2" class="section">
        <h1>2.コピペで要約</h1>
        <label>
        タイトル 
        <td class="width-100"><input type="text" name="title" class="width-100" />
      </label>
        
      <label>
        本文
        <td class="width-100"><textarea name="body" rows="5" class="width-100"></textarea></td>
      </label>
        </div>

      <p class="text-centered"><input type="submit" class="btn" value="要約"></p>
    </form>
    </div>
    </div><!-- / #page -->
    """
    return text

  def thanks_body(self):
    text="""
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
        	<div id="facebook"><div class="fb-like" data-width="110" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="false" data-send="false"></div></div><!-- / #facebook -->
            <a href="http://b.hatena.ne.jp/entry/http://shirosum.appspot.com/" class="hatena-bookmark-button" data-hatena-bookmark-title="白ヤギが自動で要約します" data-hatena-bookmark-layout="standard-balloon" data-hatena-bookmark-lang="ja" title="このエントリーをはてなブックマークに追加"><img src="http://b.st-hatena.com/images/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a><script type="text/javascript" src="http://b.st-hatena.com/js/bookmark_button.js" charset="utf-8" async></script>
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

      <a href="http://bizzlio.shiroyagi.co.jp">
        <img src="http://bizzlio.shiroyagi.co.jp/system/logos/1306/original/logo.jpg?1376467655" />
      </a>
    </div>

    <p><a href="http://shirosum.appspot.com/">もう一度要約する</a></p>       
    </div><!-- / #page -->
    """
    return text

  def footer(self):
    text="""
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
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-42448673-3', 'shirosum.appspot.com');
      ga('send', 'pageview');
    </script>
    </body>
    </html>
    """
    return text

  def summary_done_page_body(self, jres):
    
    s=''
    if jres.has_key('title'):
      s+='<h2 class="article-title text-shadow">'+jres['title']+'</h2>'
    else:
      s+='<h2 class="article-title text-shadow">タイトルが見つかりませんでした</h2>'
    if len(jres['bullets'])>0:
      s+='<p>1. '
      s+=(jres['bullets'][0][0])
      s+=('</p>')
    if len(jres['bullets'])>1:
      s+=('<p>2. ')
      s+=(jres['bullets'][1][0])
      s+=('</p>')
    if len(jres['bullets'])>2:
      s+=('<p>3. ')
      s+=(jres['bullets'][2][0])
      s+=('</p>')
    if len(jres['bullets'])>3:
      s+=('<p>4. ')
      s+=(jres['bullets'][3][0])
      s+=('</p>')
    if len(jres['bullets'])>4:
      s+=('<p>5. ')
      s+=(jres['bullets'][4][0])
      s+=('</p>')
    s=s.encode('utf-8')

    text='''
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
        	<div id="facebook"><div class="fb-like" data-width="110" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="false" data-send="false"></div></div><!-- / #facebook -->
            <a href="http://b.hatena.ne.jp/entry/http://shirosum.appspot.com/" class="hatena-bookmark-button" data-hatena-bookmark-title="白ヤギが自動で要約します" data-hatena-bookmark-layout="standard-balloon" data-hatena-bookmark-lang="ja" title="このエントリーをはてなブックマークに追加"><img src="http://b.st-hatena.com/images/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a><script type="text/javascript" src="http://b.st-hatena.com/js/bookmark_button.js" charset="utf-8" async></script>
    	    </div>
        </div>
    </header>

    <div id="section-desc">
      <h1 id="h-desc" class="text-shadow clear">要約完了 (要約率'''+str(jres['compression'])+'''%)</h1>
      <p id="desc">戦略コンサル風に言うと「この文章のポイントは３つあって・・・」要約終了しました。<br>よろしければどれくらい正確な要約になっているか評価をおねがいします。評価をいただくごとに機械学習アルゴリズムが賢くなっていきますので、今後のサービスの向上にリアルに効果があります。ご利用ありがとうございました！</p>
    </div>

    <h1 class="medium blue"></h1>
    <div id="section-2-done" class="section">'''+s+'''</div>

    <div id="section-3" class="section">
      <p>
          <form method="post" action="/sign" class="forms">
        <label><h3>アルゴリズムの向上のため評価をお願いします(ひとつ選んでください） <em class="req">*</em></h3></label>
        <ul class="forms-inline-list">
          <li><input name="evaluation" value="1" type="radio"> <label>非常に良い</label></li>
          <li><input name="evaluation" value="2" type="radio"> <label>良い</label></li>
          <li><input name="evaluation" value="3" type="radio" checked> <label>普通</label></li>
          <li><input name="evaluation" value="4" type="radio"> <label>悪い</label></li>
          <li><input name="evaluation" value="5" type="radio"> <label>非常に悪い</label></li>
        </ul>
            <input type="submit" class="btn" value="送信">
            </form>
      </p>
    </div>
     
    </div><!-- / #page -->
    '''
    return text

