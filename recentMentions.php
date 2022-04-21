<?php
	
	$name = $_GET["q"];
	$query = 'python NumberByMention.py '. $name;
	$output = exec($query);
	
	echo $output;

?>