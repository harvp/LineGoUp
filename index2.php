<!DOCTYPE html>
<!--
Colors Used:
Twitter Blue: #55ACEE
Black: #000000
Dark Gray: #303030
White: #FFFFFF
-->
<?php
	session_start();
	?>
<html lang = "en-us">
	<head>
		<meta charset = "utf8mb4">
		<meta name = "decription" content = "Twitter and stock market analytics">
		<meta name = "authors" content = "Harvey Petersen, Madeline Gesquiere">
		<meta name = "viewport" content = "width = device - width, initial-scale = 1.0">
		
		<title>Line Go Up</title>
		<style>
			html
			{
				margin: 0px, 10%;
				padding: 0;
				background: #55ACEE;
				font-family: Verdana, sans serif;
			}

			body
			{
				margin: 0;
				padding: 0;
				background: #FFFFFF;
			}
			
			.pageHeader
			{
				margin: 0px;
				background: #55ACEE;
				color: #FFFFFF;
			}
			
			h1
			{
				text-align: center;
				font-size: 30px;
				margin: 5px 10% 0px;
			}
			
			h2
			{
				text-align: center;
				font-size: 25px;
				margin: 5px 50px 0px;
			}
			
			p
			{
				background: #FFFFFF;
				margin: 5px 15%;
				text-align: center;
			}
			
			hr
			{
				margin: 0px;
			}
			
			form
			{
				text-align: center;
			}
		</style>
	</head>
	<body> 
		<section class = "pageHeader"> <!-- Page Header -->
			<h1> Line Go Up </h1>
		</section>
		<hr>
		<section> <!-- Intro Paragraph -->
			<p>
				Welcome to Line Go Up. This is an analytics tool for Twitter and the stock market. <br>
				The program gathers information on anything related to tweets and tries to find a correlation to the stock market. <br>
			</p>
		</section>
		<hr>
				<section> <!-- User Info -->
			<h2>
				Search for User Info:
			</h2>
			<p>
				Search for a user and gather information on a user.
				You can find information such as their most recent retweets,
				their most recent likes, their top tweets by tag, and a number
				of other things.
			</p>
			<form method = "POST" action = "RecentByAccChron.php">
				<input id = "searchUser" type = "text" style = "width: 300px;" placeholder = "Twitter User" name = "user" \>
				<input type = "submit"  value = "Submit" />
			</form>
			<hr>
			<form>
				<input id = "goButton" type = "button" value = "Single Tweet" style="background:#303030; color:#FFFFFF; height:50px; width:200px;" onclick = "getSingleTweet()" \>

				<input id = "goButton" type = "button" value = "Most Recent Tweets" style="background:#303030; color:#FFFFFF; height:50px; width:200px;" onclick = "getRecentByAccChron()" \>
			</form>
			<form>
				<input id = "goButton" type = "button" value = "Most Recent Likes" style="background:#303030; color:#FFFFFF; height:50px; width:200px" onclick = "getRecentByAccLikes()" \>

				<input id = "goButton" type = "button" value = "Most Recent Retweets" style="background:#303030; color:#FFFFFF; height:50px; width:200px" onclick = "getRecentByAccRetweets()"\>
			</form>
			<form>
				<input id = "goButton" type = "button" value = "Top Tweets By Mention" style="background:#303030; color:#FFFFFF; height:50px; width:200px" onclick = "getTopTweetsByMention()"\>
	
				<input id = "goButton" type = "button" value = "Top Tweets By Tag" style="background:#303030; color:#FFFFFF; height:50px; width:200px" onclick = "getTopTweetsByTag()"\>
			</form>
		</section>
		<hr>
		 
		<section> <!-- Output -->
			<h2>
				Function Output:
			</h2>
			<p id = "output">
				Nothing to display!
			</p>
		</section>

		<hr>
		<section> <!-- Javascript to access scripts -->
			<script async src="https://platform.twitter.com/widgets.js"></script>
			<script>
				function getSingleTweet()
				{
					toPHP("GetSingleTweetByAcc.php", "output", "")
				}
				function getRecentByAccChron()
				{
					toPHP("RecentByAccChron.php", "output", "")	
				}	
				function getRecentByAccLikes()
				{
					toPHP("RecentByAccLikes.php", "output", "")
				}
				function getRecentByAccRetweets()
				{
					toPHP("RecentByAccRetweet.php", "output", "")
				}
				function getTopTweetsByMention()
				{
					toPHP("TopTweetsByMention.php", "output", "")
				}
				function getTopTweetsByTag()
				{
					toPHP("TopTweetsByTag.php", "output", "")
				}

				function pageLoad()
				{
					
				}

				function toPHP(dest, output, parameter)
				{
					var temp = parameter;
					temp.trim();
					if(temp != "")
					{
						parameter.replace(/ /g,"_");
						dest += "?q=" + parameter;
					}
				
					var xmlhttp = new XMLHttpRequest();
					xmlhttp.onreadystatechange = function()
					{
						if(this.readyState == 4 && this.status == 200)
						{
							document.getElementById(output).innerHTML = this.responseText;
							var script= document.createElement('script');
      						script.src= "https://platform.twitter.com/widgets.js";
							document.getElementById(output).appendChild(script);
						}
					}
					xmlhttp.open("GET", dest, true);
					xmlhttp.send();
				}
				
			</script>
		</section>

	</body>

</html>