#_/_/_/_/_/_/_/_/#
#    �Ĕ���      #
#_/_/_/_/_/_/_/_/#

sub BUY {

	$ksub2=0;
	if($csub){
		if($cnum > 3000){
			$cnum = 3000;
		}
		if(!$cno){
			if($kgold >= $cnum){
				if($cnum * $csub){
					$kadd = int((2-$csub) * $cnum);
				}else{
					$kadd = 0;
				}
				$kgold -= $cnum;
				$krice += $kadd;
				&K_LOG("$mmonth��:�y���l�z�F��$cnum���x������$kadd�̕Ă𔃂��܂����B");
				$kint_ex++;
				$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$ktec1,$ktec2,$ktec3,$kvsub1,$kvsub2,";
			}else{
				&K_LOG("$mmonth��:�y���l�z�F������������܂���B");
			}
		}else{
			if($krice > $cnum){
				$kadd = int($cnum * $csub);
				$krice -= $cnum;
				$kgold += $kadd;
				&K_LOG("$mmonth��:�y���l�z�F$cnum�̕Ă𔄂���$kadd�̋��𔃂��܂����B");
				$kint_ex++;
				$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$ktec1,$ktec2,$ktec3,$kvsub1,$kvsub2,";
			}else{
				&K_LOG("$mmonth��:�y���l�z�F�Ă�����܂���B");
			}
		}
	}

}
1;