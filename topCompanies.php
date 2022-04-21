
<?php
	
	$query = 'python Top10.py';
	$output = exec($query);
	
	echo $output;

?>