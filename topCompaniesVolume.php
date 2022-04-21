
<?php
	
	$query = 'python Top10ByVol.py';
	$output = exec($query);
	
	echo $output;

?>