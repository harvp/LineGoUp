<?php

	$outputStr = "<h3>Recent Tweets By Account: Most Liked</h3>";
	$name = $_GET["q"];
	$query = 'python RecentByAccLikes.py '. $name;
	$output = exec($query);
	
	echo($outputStr);
	echo $output;

?>

