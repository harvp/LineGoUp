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
			<h1><img src = "https://raw.githubusercontent.com/harvp/LineGoUp/main/logo2.png" alt = "logo" height = "100" width = "300">
				<img src = "https://raw.githubusercontent.com/harvp/LineGoUp/main/logo.png" alt = "logo" height = "100" width = "100"></h1>
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
				Search for a user using their Twitter account handle and stock ticker symbol.
				You can find information such as their most recent tweets,
				a report on their stocks from the last seven days, and a number
				of other things.
			</p>
			<form>
				<input id = "searchUser" type = "text" class = "text" placeholder = "Twitter User" name = "user" \><input id = "searchTicker" type = "text" class = "text" placeholder = "Stock Ticker" name = "ticker" \>
			</form>
			
			<hr>
			<form>
		
				<input id = "goButton" type = "button" value = "User's Recent Tweets" class = "button" onclick = "recentTweets()" \>

				<input id = "goButton" type = "button" value = "Stock History" class = "button" onclick = "stockHistory()" \>

				<input id = "goButton" type = "button" value = "Volatility Report" class = "button" onclick = "volatilityReport()"\>
			</form>
			<form>
				<input id = "goButton" type = "button" value = "Most Volatile - Trade" class = "button" onclick = "top10Companies()"\>

				<input id = "goButton" type = "button" value = "Most Volatile - Volume" class = "button" onclick = "getTopTweetsByTag()"\>

<<<<<<< HEAD
				<input id = "goButton" type = "button" value = "Volatility By Mentions" class = "button" onclick = "recentMentions()" \>
=======
				<input id = "goButton" type = "button" value = "Most Recent Mentions" class = "button" onclick = "getTopTweetsByMention()" \>
>>>>>>> b08a70e9a95ff618f2e0b9669d23aca3484aa282
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

			    function recentTweets()
			    {
					var user = document.getElementById("searchUser").value;
					var temp1 = user;
					if(temp1.trim()!= "")
						toPHP("RecentByAccChron.php", "output", user, "", 1);	
			    }
			    function stockHistory()
			    {
			    	var ticker = document.getElementById("searchTicker").value;
					var temp1 = ticker;
					if(temp1.trim()!= "")
						toPHP("StockHistory.php", "output", "", ticker, 2);
			    }
			    function volatilityReport()
			    {
			    	var user = document.getElementById("searchUser").value;
					var ticker = document.getElementById("searchTicker").value;
					var temp1 = user;
					var temp2 = ticker;
					if((temp1.trim()!= "") && (temp2.trim()!= ""))
						toPHP("volatilityReport.php", "output", user, ticker, 0)	
			    }
			    function top10Companies()
			    {
			    	toPHP("topCompanies.php", "output", "", "", 3)
			    }
<<<<<<< HEAD
				function recentMentions()
				{
					var user = document.getElementById("searchUser").value;
					var ticker = document.getElementById("searchTicker").value;
					var temp1 = user;
					var temp2 = user;
					if((temp1.trim()!= "") && (temp2.trim()!= ""))
						toPHP("recentMentions.php", "output", user, ticker, 0)	
				}
				function getRecentByAccChron()
				{
					
				}	
				function getRecentByAccLikes()
				{
					
				}
				function getRecentByAccRetweets()
				{
					
				}
=======
>>>>>>> b08a70e9a95ff618f2e0b9669d23aca3484aa282
				function getTopTweetsByMention()
				{
					
				}
				function getTopTweetsByTag()
				{
					
				}

				function pageLoad()
				{
					
				}

				function toPHP(dest, output, user, ticker, mode)
				{
					if (mode == 0)
					{
						var temp = user;
						temp.trim();
						if(temp != "")
						{
							user.replace(/ /g,"_");
							dest += "?q=" + user;
						}
						temp = ticker;
						temp.trim();
						if(temp != "")
						{
							user.replace(/ /g,"_");
							dest += " " + ticker;
						}
					}
					if (mode == 1){
						var temp = user;
						temp.trim();
						if(temp != "")
						{
							user.replace(/ /g,"_");
							dest += "?q=" + user;
						}
					}
					if (mode == 2){
						var temp = ticker;
						temp.trim();
						if(temp != "")
						{
							user.replace(/ /g,"_");
							dest += "?q=" + ticker;
						}	
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