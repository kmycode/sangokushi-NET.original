#_/_/_/_/_/_/_/_/_/_/#
#      �W��          #
#_/_/_/_/_/_/_/_/_/_/#

sub SYUUGOU {

	$ksub2=0;
	$uhit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
		if("$uid" eq "$kid" && $unit_id eq $kid){$uhit=1;last;}
	}
	if(!$uhit){
		&K_LOG("$mmonth��:�����������s�ł��܂���B");
	}else{

		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
			if($unit_id eq $kid && $uid ne $unit_id){
				open(IN,"./charalog/main/$uid.cgi");
				@E_DATA = <IN>;
				close(IN);
				($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);								
				$epos = $kpos;
				if($eid ne ""){
					&E_LOG2("$mmonth��:$uunit_name�����͑����̖��߂ɂ��$town_name[$kpos]�ɏW���������܂����B");
					&ENEMY_INPUT;
				}
			}elsif($unit_id eq $kid && $uid eq $unit_id){
				$unit_name = $uunit_name;
			}
		}
		$klea_ex++;
		$kcex+=10;
		$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
		&K_LOG("$mmonth��:$unit_name������$town_name[$kpos]�ɏW�������܂����B");
	}

}
1;