<?php
	
	$name = $_GET["q"];
	$query = 'python Financial.py '. $name;
	$output = exec($query);
	echo $output;
	
	

?>