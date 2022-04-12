
	<?php
	
	$Name = "microsoft";
	if(isset($_POST["user"])){
   		$Name = $_POST["user"];
	}

	$command = escapeshellcmd('python RecentByAccChron.py'." ".$Name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


