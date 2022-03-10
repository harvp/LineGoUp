<?php
	
	$command = escapeshellcmd('python RecentByAccLikes.py a');
	$output = shell_exec($command);
	$outputStr = "<h3>Recent Tweets By Account: Most Liked</h3>";
 	$outputStr .="<blockquote class=\"twitter-tweet\"><p>Stephanie J. Creary, Wharton School Assistant Professor, shares insights on identity and inclusion. <a>pic.twitter.com/cwZbOQNs1O</a></p>&mdash; Microsoft (@Microsoft) <a href=\"";
 	$outputStr .= $output;
 	$outputStr .= "\">February 23, 2022</a></blockquote>";	

	echo($outputStr);
?>

