<!DOCTYPE html>
<!--
Colors Used:
Twitter Blue: #55ACEE
White: #FFFFFF
Dark Slate Blue: #483D8B
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
				font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
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
				padding: 5px;
				background: #55ACEE;
				color: #FFFFFF;
			}
			
			h1
			{
				text-align: center;
				font-size: 35px;
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
				border-bottom: solid 2px #483D8B;
			}
			
			form
			{
				text-align: center;
			}
			
			.button
			{
				background: #483D8B; 
				color: #FFFFFF; 
				height: 50px; 
				width: 200px;
				border-radius: 8px;
				margin: 10px;
				font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
			}
			
			.button:hover 
			{
  				background-color: #55ACEE;
			}

			.text 
			{
				background-color: #E3E3E3;
				width: 300px;
				margin: 10px;
			}

			.text:hover
			{
				background-color: #FFFFFF;
			}
		</style>
	</head>
	<body> 
		<section class = "pageHeader"> <!-- Page Header -->
			<h1><img src = "https://raw.githubusercontent.com/harvp/LineGoUp/main/logo2.png" alt = "logo" height = "100" width = "100"></h1>
			<h1><img src = "https://raw.githubusercontent.com/harvp/LineGoUp/main/logo.png" alt = "logo" height = "100" width = "100"></h1>
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
			<form>
				<input id = "searchUser" type = "text" class = "text" placeholder = "Twitter User" name = "user" \>
			</form>
			<hr>
			<form>
				<input id = "goButton" type = "button" value = "Single Tweet" class = "button" onclick = "getSingleTweet()" \>

				<input id = "goButton" type = "button" value = "Most Recent Tweets" class = "button" onclick = "getRecentByAccChron()" \>
			</form>
			<form>
				<input id = "goButton" type = "button" value = "Most Recent Likes" class = "button" onclick = "getRecentByAccLikes()" \>

				<input id = "goButton" type = "button" value = "Most Recent Retweets" class = "button" onclick = "getRecentByAccRetweets()"\>
			</form>
			<form>
				<input id = "goButton" type = "button" value = "Top Tweets By Mention" class = "button" onclick = "getTopTweetsByMention()"\>
	
				<input id = "goButton" type = "button" value = "Top Tweets By Tag" class = "button" onclick = "getTopTweetsByTag()"\>
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
					var entry = document.getElementById("searchUser").value
					var temp = entry;
					if(temp.trim()!= "")
						toPHP("GetSingleTweetByAcc.php", "output", entry)
				}
				function getRecentByAccChron()
				{
					var entry = document.getElementById("searchUser").value
					var temp = entry;
					if(temp.trim()!= "")
						toPHP("RecentByAccChron.php", "output", entry)	
				}	
				function getRecentByAccLikes()
				{
					var entry = document.getElementById("searchUser").value
					var temp = entry;
					if(temp.trim()!= "")
						toPHP("RecentByAccLikes.php", "output", entry)
				}
				function getRecentByAccRetweets()
				{
					var entry = document.getElementById("searchUser").value
					var temp = entry;
					if(temp.trim()!= "")
						toPHP("RecentByAccRetweet.php", "output", entry)
				}
				function getTopTweetsByMention()
				{
					var entry = document.getElementById("searchUser").value
					var temp = entry;
					if(temp.trim()!= "")
						toPHP("TopTweetsByMention.php", "output", entry)
				}
				function getTopTweetsByTag()
				{
					var entry = document.getElementById("searchUser").value
					var temp = entry;
					if(temp.trim()!= "")
						toPHP("TopTweetsByTag.php", "output", entry)
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