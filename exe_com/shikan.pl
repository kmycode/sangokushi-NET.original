#_/_/_/_/_/_/_/_/_/_/#
#       �d  ��       #
#_/_/_/_/_/_/_/_/_/_/#

sub SHIKAN {

	$ksub2=0;
	&COUNTRY_DATA_OPEN($kcon);
	if($xcid eq 0){
		if($cou_name[$cnum] eq ""){
			&K_LOG("$mmonth��:���̍��ւ͎d���ł��܂���B");
		}else{
			if(@B_LIST eq "0"){
				open(IN,"$LOG_DIR/black_list.cgi");
				@B_LIST = <IN>;
				close(IN);
			}
			$b_hit=0;
			foreach(@B_LIST){
				($bid,$bcon,$bname,$bsub) = split(/<>/);
				if($bid eq $kid && $bcon eq $kcon){
					$b_hit=1;
				}
			}
			if($b_hit){
				&K_LOG("$mmonth��:$cou_name[$cnum]�֎d���͋��ۂ���܂���");
			}else{
				$kcon = $cnum;
				&K_LOG("$mmonth��:$cou_name[$cnum]�֎d�����܂����B");
				&MAP_LOG("$mmonth��:$kname��$cou_name[$cnum]�֎d�����܂����B");
			}
		}
	}else{
		&K_LOG("$mmonth��:���������łȂ���Ύd���ł��܂���B");
	}

}
1;