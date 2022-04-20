<?php
	
	$name = $_GET["q"];
	$query = 'python NumberCrunch.py '. $name;
	$output = exec($query);
	
	echo $output;
	

?>
