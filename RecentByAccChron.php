
	<?php
	
	$Name = "microsoft";
	if(isset($_POST["searchUser"])){
   		$Email = $_POST["searchUser"];
	}

	$command = escapeshellcmd('python RecentByAccChron.py'." ".$Name);
	$output = exec($command);
	$counter = $output;
	$stringBuilder = '<div>';
	
	echo $output;
	

?>


