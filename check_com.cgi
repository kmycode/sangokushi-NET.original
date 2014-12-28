# _/_/_/_/_/_/_/_ #
#     �X�V����    #
# _/_/_/_/_/_/_/_ #
sub CHECK_COM{

	# Command list
	require './ini_file/com_list.ini';

	&D_F_LOCK;
	if (!-e $lockfile2) {&ERR2("�t�@�C�����b�N����Ă��܂���B");}

	open(IN,"$TOWN_LIST");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$UNIT_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@UNI_DATA = <IN>;
	close(IN);

	# �s�s�f�[�^��z��Ɋi�[
	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$town_get[$z2con] += 1;
		$town_num[$z2con] += $z2num;
		$town_nou[$z2con] += $z2nou;
		$town_syo[$z2con] += $z2syo;
		$zc++;
	}

	# PLAYER DATA��z��Ɋi�[
	$dir="./charalog/main";
	if($mmonth eq "1" || $mmonth eq "7"){
		opendir(dirlist,"$dir");
		while($file = readdir(dirlist)){
			if($file =~ /\.cgi/i){
				if(!open(page,"$dir/$file")){
					&ERR2("�t�@�C���I�[�v���G���[�I");
				}
				@page = <page>;
				close(page);
				($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex) = split(/<>/,$page[0]);
				$cou_num[$kcon]++;
				$cex_total[$kcon]+=$kcex;
				push(@CL_DATA,"@page<br>");
			}
		}
		closedir(dirlist);
	}

	opendir(dirlist,"$dir");
	$kup_date=0;
	$thit=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("�t�@�C���I�[�v���G���[�I");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$page[0]);
			if($kdate + $TIME_REMAKE < $date && $mtime > $kdate){
				$thit=1;
				($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);
				if($mmonth eq "1"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
					$kadd  = int(($ksal * $kcex / $cex_total[$kcon]) + $kcex * 1.3);
					}
					$s_num = int($kclass / $LANK);
					if($s_num > 20){$s_num = 20;}
					if($kadd > 1000 + $s_num * 150){$kadd=1000 + $s_num * 150;}
					$kgold += $kadd;
					$k_ex_fol= ($kclass % $LANK)+$kcex;
					$kclass += $kcex;
					if($k_ex_fol > $LANK){
						$s_num = int($kclass / $LANK);
						if($s_num > 20){$s_num = 20;}
						$nadd = int(rand(3));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "����";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "�m��";
						}else{
							$klea++;
							$add_m = "������";
						}
						$max_sal = 1000 + $s_num * 150;
						&K_LOG("$mmonth��:�y<font color=red>���i</font>�z$add_m���P�オ��܂����I");
						&K_LOG("$mmonth��:�y<font color=red>���i</font>�z$LANK[$s_num]�ɂȂ����I���^�̍ő�x���z��<font color=red> $max_sal </font>�ɂȂ����I");

					}
					$kcex = 0;
					&K_LOG("$mmonth��:�ŋ���<font color=red>$kadd</font>�̋��𒥎����܂����B");
				}elsif($mmonth eq "7"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
						$kadd  = int(($ksal * $kcex / $cex_total[$kcon]) + $kcex * 1.3);
					}
					$s_num = int($kclass / $LANK);
					if($s_num > 20){$s_num = 20;}
					if($kadd > 1000 + $s_num * 150){$kadd=1000 + $s_num * 150;}
					$krice += $kadd;
					$k_ex_fol= ($kclass % $LANK)+$kcex;
					$kclass += $kcex;
					if($k_ex_fol > $LANK){
						$s_num = int($kclass / $LANK);
						if($s_num > 20){$s_num = 20;}
						$nadd = int(rand(3));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "����";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "�m��";
						}else{
							$klea++;
							$add_m = "������";
						}
						$max_sal = 1000 + $s_num * 150;
						&K_LOG("$mmonth��:�y<font color=red>���i</font>�z$add_m���P�オ��܂����I");
						&K_LOG("$mmonth��:�y<font color=red>���i</font>�z$LAMK[$s_num]�ɂȂ����I���^�̍ő�x���z��<font color=red> $max_sal </font>�ɂȂ����I");
					}
					$kcex = 0;
					&K_LOG("$mmonth��:���n��<font color=red>$kadd</font>�̐H�������n���܂����B");
				}
				open(IN,"./charalog/command/$kid\.cgi");
				@COM_DATA = <IN>;
				close(IN);
				($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[0]);

				$kdate += $TIME_REMAKE;
				&CHARA_MAIN_INPUT;
				splice(@COM_DATA,0,1);
				push(@COM_DATA,"<><><><><><><>\n");

				open(OUT,">./charalog/command/$kid\.cgi");
				print OUT @COM_DATA;
				close(OUT);

				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$kpos]);
				if($zcon eq "$kcon" || $cid eq "20" || $cid eq "21" || $cid eq "27" || $cid eq "0" || $cid eq ""){

					$kprodmg = 0;
					if($kbook ne "" && $kbook ne 0){
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($kproname,$kproval,$kprodmg) = split(/<>/,$PRO_DATA[$kbook]);
					}
					if($cid eq $NOUGYOU){
						if(!$nougyou){
							require "$EXE/nougyou.pl";
							$nougyou = TRUE;
						}
						&NOUGYOU;
					}elsif($cid eq $SYOUGYOU){
						if(!$syougyou){
							require "$EXE/syougyou.pl";
							$syougyou = TRUE;
						}
						&SYOUGYOU;
					}elsif($cid eq $SHIRO){
						if(!$shiro){
							require "$EXE/shiro.pl";
							$shiro = TRUE;
						}
						&SHIRO;
					}elsif($cid eq $RICE_GIVE){
						if(!$rice_give){
							require "$EXE/rice_give.pl";
							$rice_give = TRUE;
						}
						&RICE_GIVE;
					}elsif($cid eq $GET_SOL2){
						if(!$get_sol){
							require "$EXE/get_sol.pl";
							$get_sol = TRUE;
						}
						&GET_SOL;
					}elsif($cid eq $KUNREN){
						$ksub2=0;
						$kgat += int($klea/6 + rand($klea/6));
						if($kgat > 100){
							$kgat = 100;
						}
						$kcex += 15;
						&K_LOG("$mmonth��:���m�̌P���x��<font color=red>$kgat</font>�ɂȂ�܂����B");
						$klea_ex++;
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
					}elsif($cid eq $TOWN_DEF){
						if(!$town_def){
							require "$EXE/town_def.pl";
							$town_def = TRUE;
						}
						&TOWN_DEF;
					}elsif($cid eq "18"){
						$ksub2=0;
						($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$cnum]);
						if($zcon eq $kcon){
							&K_LOG("$mmonth��:�����ɂ͍U�߂��܂���B");
						}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
							&K_LOG("$mmonth��:$zname�ɂ͗אڂ��Ă��܂���B");
						}else{
							if(!$battle_check){
								require 'battle.cgi';
								$battle_check = 1;
							}
							&BATTLE;
						}
					}elsif($cid eq $BUY2){
						if(!$buy){
							require "$EXE/buy.pl";
							$buy = TRUE;
						}
						&BUY;
					}elsif($cid eq "20"){
						$ksub2=0;
						$zhit=0;
						foreach(@z){
							if($_ eq $cnum){$zhit=1;}
						}
						if($zhit){
							$kpos = $cnum;
							$klea_ex++;
							if($xcid ne "0"){$kcex += 20;}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth��:$town_name[$cnum]�ֈړ����܂����B");
						}else{
							&K_LOG("$mmonth��:$town_name[$cnum]�ֈړ��o���܂���B���݈ʒu�F$zname");
						}
					}elsif($cid eq $SHIKAN){
						if(!$shikan){
							require "$EXE/shikan.pl";
							$shikan = TRUE;
						}
						&SHIKAN;
					}elsif($cid eq "22"){
						$ksub2=0;
						open(IN,"$ARM_LIST");
						@ARM_DATA = <IN>;
						close(IN);
						($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$cnum]);
						($armname2,$armval2) = split(/<>/,$ARM_DATA[$karm]);
						$armval2 = int($armval2 * 0.6);
						if($armval > $kgold + $armval2){
							&K_LOG("$mmonth��:������������܂���B$armname ��:$armval");
						}else{
							$kgold += $armval2;
							$kgold -= $armval;
							$karm = $cnum;
							&K_LOG("$mmonth��:����F$armname2����<font color=red>$armval2</font>�Ŕ���$armname���w�����܂����B");
						}
					}elsif($cid eq "23"){
						$ksub2=0;
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($proname,$proval,$prodmg,$prowei,$proele,$prosta,$proclass,$protownid) = split(/<>/,$PRO_DATA[$cnum]);
						($proname2,$proval2) = split(/<>/,$PRO_DATA[$kbook]);
						$proval2 = int($proval2 * 0.6);
						if($proval > $kgold + $proval2){
							&K_LOG("$mmonth��:������������܂���B$proname ��:$proval");
						}else{
							$kgold += $proval2;
							$kgold -= $proval;
							$kbook = $cnum;
							&K_LOG("$mmonth��:���ЁF$proname���w�����܂����B");
						}
					}elsif($cid eq $GET_MAN2){
						if(!$get_man){
							require "$EXE/get_man.pl";
							$get_man = TRUE;
						}
						&GET_MAN;
					}elsif($cid eq $TANREN2){
						if(!$tanren){
							require "$EXE/tanren.pl";
							$tanren = TRUE;
						}
						&TANREN;
					}elsif($cid eq $SYUUGOU){
						if(!$syuugou){
							require "$EXE/syuugou.pl";
							$syuugou = TRUE;
						}
						&SYUUGOU;
					}elsif($cid eq $TEC){
						if(!$tec){
							require "$EXE/tec.pl";
							$tec = TRUE;
						}
						&TEC;
					}elsif($cid eq $SHIRO_TAI){
						if(!$shiro_tai){
							require "$EXE/shiro_tai.pl";
							$shiro_tai = TRUE;
						}
						&SHIRO_TAI;
					}else{
						$ksub2++;
						if($ksub2 > $DEL_TURN){
							unlink("./charalog/main/$kid\.cgi");
							unlink("./charalog/log/$kid\.cgi");
							unlink("./charalog/command/$kid\.cgi");
							&MAP_LOG("[���u]�F$kname�͍폜����܂����B");
							next;
						}
						&K_LOG("$mmonth��:�������s���܂���ł����B");
					}

				}else{
					&K_LOG("$mmonth��:�����ł͂���܂���B");
				}

				$krice -= $ksol;
				if($krice < 0){
					&K_LOG("$mmonth��:<font color=red>�y�E���z</font>:�Ă��x�����������E�����܂����I");
					$ksol = 0;
					$krice = 0;
				}

				$uhit=0;
				if($kstr_ex >= 10){
					$kstr++;
					$kstr_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth��:<font color=red>�y�㏸�z</font>:$kname�̕��͂��P�オ�����I");
				}
				if($kint_ex >= 10){
					$kint++;
					$kint_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth��:<font color=red>�y�㏸�z</font>:$kname�̒m�͂��P�オ�����I");
				}
				if($klea_ex >= 10){
					$klea++;
					$klea_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth��:<font color=red>�y�㏸�z</font>:$kname�̓����͂��P�オ�����I");
				}
				if($kcha_ex >= 10){
					$kcha++;
					$kcha_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth��:<font color=red>�y�㏸�z</font>:$kname�̐l�]���P�オ�����I");
				}
				if($uhit){
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
				}

				&CHARA_MAIN_INPUT;

				if($ACT_LOG){
					($qsec,$qmin,$qhour,$qday) = localtime($kdate);
					unshift(@ACT_DATA,"$kname���X�V \($qday�� $qhour:$qmin:$qsec\)\n");
				}
				$kup_date++;
				if($kup_date > $ENTRY_MAX){last;}
			}
		}
	}
	if($thit){
		&lock("xxx","1") or &ERR2("�t�@�C�����b�N�Ɏ��s���܂����B");
		&SAVE_DATA($TOWN_LIST,@TOWN_DATA);
		&unlock("xxx");
	}

	closedir(dirlist);
	&D_UNLOCK_FILE;
}


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/       LOG�̏�������      _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub E_LOG2 {

	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		unshift(@E_LOG2,"$_[0]($mday��$hour��$min��)\n");
		splice(@E_LOG2,20);

		open(OUT,">./charalog/log/$eid\.cgi");
		print OUT @E_LOG2;
		close(OUT);
	}
}

sub K_LOG2 {

	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	unshift(@K_LOG2,"$_[0]($mday��$hour��$min��)\n");
	splice(@K_LOG2,20);
	open(OUT,">./charalog/log/$kid\.cgi");
	print OUT @K_LOG2;
	close(OUT);
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/       �����v�Z           _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub SALARY {

	$ksal=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
			if($mmonth eq "1"){
				$ksal += int($z2syo * 8 * $z2num / 10000);
			}elsif($mmonth eq "7"){
				$ksal += int($z2nou * 8 * $z2num / 10000);
			}
		}
	}

}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#       FILE LOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub D_F_LOCK {

	local($retry)=1;
	if (-e $lockfile2) {
		local($mtime) = (stat($lockfile2))[9];
		if ($mtime && $mtime < time - 60) { &D_UNLOCK_FILE; }
	}

	while (!mkdir($lockfile2, 0755)) {
		if (--$retry <= 0) { &ERR2("File lock error!<BR>�f�[�^�X�V���ł��B���΂炭���҂����������B");
}
		sleep(1);
	}
}


# DATA LOCK #
sub lock #($file_name, $use_lock)
{
	local($file_name, $use_lock) = @_;
	local($lock_flag) = $file_name . ".lock";

	if ($use_lock) {
	local($i) = 0;
#	return -1 if (!-f $file_name);
	rmdir($lock_flag) if (-d $lock_flag && time - (stat($lock_flag))[9] > 60);
	while(!mkdir($lock_flag, 0755)) {
	select(undef, undef, undef, 0.05);
		return 0 if (++ $i >= 100);
		}
		return 1;
 	}
 	return 1;
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#     FILE UNLOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub D_UNLOCK_FILE
{
  rmdir("$lockfile2");
}

sub unlock
{
  rmdir("$_[0].lock") if (-d "$_[0].lock");
}

1;