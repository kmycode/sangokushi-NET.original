#!/usr/bin/perl

#################################################################
#   �y�Ɛӎ����z                                                #
#    ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B         #
#    �܂��ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B       #
#################################################################

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.pl';
require 'check_com.cgi';

if($MENTE) { &ERR2("�X�N���v�g�`�F�b�N�̈׈ꎞ�I�ɒ�~���܂��B"); }
&DECODE;
&INDEX;

#_/_/_/_/_/_/_/_/_/#
#_/  INDEX���   _/#
#_/_/_/_/_/_/_/_/_/#

sub INDEX {

	$date = time();
	$month_read = "$LOG_DIR/date_count.cgi";
	open(IN,"$month_read") or &ERR2("Can\'t file open!:month_read");
	@MONTH_DATA = <IN>;
	close(IN);
	&TIME_DATA;

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=008800>��</font>$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$D_MES .= "<font color=000088>��</font>$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$old_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "$LOG_DIR/act_log.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>��</font>$ACT_DATA[$p]<BR>";$p++;}
		$ACT_MES = "<TR><TD bgcolor=#EFE0C0 colspan=\"2\" width=80% height=20><font color=#8E4C28 size=2>$A_MES</font></TD></TR>";

	}

	open(IN,"$TOWN_LIST") or &ERR2('Can\'t file open!:month_read:TOWN_LIST');
	@TOWN_DATA = <IN>;
	close(IN);
	($zwname,$wzc)=split(/<>/,$TOWN_DATA[0]);
	$zzhit=0;
	foreach(@TOWN_DATA){
		($zwname,$zwcon)=split(/<>/);
		if($wzc ne $zwcon){$zzhit=1;}
		$wzc = $zwcon;
	}

	# PLAYER DATA UPDATE
	&CHECK_COM;

	# MASTER DATA UPDATE
	if($mtime + $TIME_REMAKE < $date){
		if($mtime eq ""){
			$mtime = $date;
			&MAP_LOG("�Q�[���v���O�������J�n���܂����B");
		}else{
			$mtime += $TIME_REMAKE;
		}
		$mmonth++;
		if($mmonth > 12){
			$myear++;
			$mmonth=1;
		}
		unshift(@month_new,"$myear<>$mmonth<>$mtime<>\n");
		if($ACT_LOG){
			($qsec,$qmin,$qhour,$qday) = localtime($mtime);
			unshift(@ACT_DATA,"===============\[$myear�N$mmonth��\]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('�t�@�C�����J���܂���ł����Berr no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY �f�[�^���������߂܂���B');
		print OUT @NEW_COU_DATA;
		close(OUT);

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("$mmonth��:<font color=orange>�ŋ�</font>�Ŋe�����ɋ��^���x�����܂����B");
			$b_hit = 1;
		}elsif($mmonth eq "7"){
			&MAP_LOG("$mmonth��:<font color=orange>���n</font>�Ŋe�����ɕĂ��x�����܂����B");
			$b_hit = 1;
		}

		# EVENT ACTION
		$eve_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);
		$ihit=0;
		if(!int(rand(40))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���Ȃ��̑�Q�������P���܂����I");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���Ȃ��̑�Q�������P���܂����I");
			}elsif($ino eq 1){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�^����������܂����I�e�n�Ŕ�Q���o�Ă��܂��I");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�^����������܂����I�e�n�Ŕ�Q���o�Ă��܂��I");
			}elsif($ino eq 2){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�u�a�����s���Ă���悤�ł��B�X�̐l�X���ꂵ��ł��܂��B�B");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�u�a�����s���Ă���悤�ł��B�X�̐l�X���ꂵ��ł��܂��B�B");
			}elsif($ino eq 3){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���N�͖L��ɂȂ肻���ł��B");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���N�͖L��ɂȂ肻���ł��B");
			}elsif($ino eq 4){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]��n�k��������܂����I");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]��n�k��������܂����I");
			}elsif($ino eq 5){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�e���̏��X��������Ă��܂��B");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�e���̏��X��������Ă��܂��B");
			}
		}
		if($b_hit){
			@NEW_TOWN_DATA=();
			foreach(@TOWN_DATA){
				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/);
				# ����ϓ�
				if(!int(rand(2.0))){
					$zsouba += int(rand(0.5)*100)/100;
					if($zsouba > 1.2){
						$zsouba = 1.2;
					}
				}else{
					$zsouba -= int(rand(0.5)*100)/100;
					if($zsouba < 0.8){
						$zsouba = 0.8;
					}
				}
				if($zpri >= 50){
					$znum_add = int(80 * ($zpri - 50));
					if($znum_add < 500){$znum_add=500;}
					$znum += $znum_add;
					if($znum > $NOU_MAX){$znum=$NOU_MAX;}
				}else{
					$znum -= int(80 * (50 - $zpri));
					if($znum < 0){$znum=0;}
				}
				# EVENT
				if($ihit){
					if($ino eq 0){
						$znou = int($znou * 0.8);
					}elsif($ino eq 1){
						$znou = int($znou * 0.9);
						$zsyo = int($zsyo * 0.9);
						$zshiro = int($zshiro * 0.9);
					}elsif($ino eq 2){
						$znum = int($znum * 0.8);
					}elsif($ino eq 3){
						$znou = int($znou * 1.2);
						if($znou > $znou_max){$znou=$znou_max;}
					}elsif($ino eq 4){
						$znou = int($znou * 0.8);
						$zsyo = int($zsyo * 0.8);
						$zshiro = int($zshiro * 0.8);
						$znum = int($znum * 0.9);
					}elsif($ino eq 5){
						$zsyo = int($zsyo * 1.1);
						if($zsyo > $zsyo_max){$zsyo=$zsyo_max;}
						$znum = int($znum * 1.1);
						if($znum > $NOU_MAX){$znum=$NOU_MAX;}
					}
				}
				push(@NEW_TOWN_DATA,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
			}
			&SAVE_DATA($TOWN_LIST,@NEW_TOWN_DATA);
		}
		&SAVE_DATA($month_read,@month_new);
	}
	if($ACT_LOG){
		if(@ACT_DATA > 800) { splice(@ACT_DATA,800); }
		open(OUT,">$actfile");
		print OUT @ACT_DATA;
		close(OUT);
	}

	$MESS1 = "<A href=\"$FILE_CONTNUE\">�yCONTNUE�z</a>";
	$MESS2 = "<A href=\"$FILE_ENTRY\">�y�V�K�o�^�z</a>";
	&COUNTER;
	$new_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);

	&HEADER;
	print <<"EOM";
[<a href=./i-index.cgi>�g�їp</a>]<CENTER>
<TABLE WIDTH="100%" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<TABLE border=0 width=80% height=100% cellspacing=1><TBODY>
<TR><TD align=center><p><TABLE width=80% height=140 bgcolor=#DECCA8>
<TR><TD align=center bgcolor=EFE0C0><h1><font color=442200>$GAME_TITLE</font></h1><p>
<font size=2 color=#9c5a4b><p><B>[$new_date]</b><BR>����̍X�V�܂� <B>$next_time</B> ��<BR></font>
</TD></TR></TABLE>

<p align="center">
<table bgcolor=$TABLE_C align=center border=0><form action="$FILE_STATUS" method="POST">
<input type="hidden" name="mode" value="STATUS">
<TR><TH bgcolor=$TD_C2 height=5>USER ID</TH><td><input type="text" size="10" name="id" value="$_id"></td></TR>
<TR><TH bgcolor=$TD_C2 height=5>PASS WORD</tH><td><input type="password" size="10" name="pass" value="$_pass"></TD></TR>
<TR><td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="���O�C��"></td></tr></table></form>
$MESS2 
<A href="$FILE_RANK">�y�o�^�����ꗗ�z</A> 
<A href="./manual.html">�y�������z</A> 
<A href="./map.cgi">�y���͐}�z</A> <p>
<A href="$HOME_URL">�y$HOME�z</A>
<A href="$BBS1_URL">�y$BBS1�z</A>
<A href="$LINK2_URL">�y$LINK2�z</A>
�ő�o�^�l��($ENTRY_MAX�l)</font><BR>

<TABLE width=100% BGCOLOR=$TABLE_C  cellspacing=1><TBODY>$mess</TBODY></TABLE>
<CENTER><HR size=0><p align=right>[<font color=8E6C68>TOTAL ACCESS<font color=red><B> $total_count </font></B>HIT</font>]<BR>
</TD></TR>
<TR><TD bgcolor=#EFE0C0 colspan="2" width=80% height=20><font color=#8E4C28 size=2>$S_MES</font></TD></TR>
<TR><TD bgcolor=#EFE0C0 colspan="2" width=80% height=20><font color=#8E4C28 size=2>$D_MES</font></TD></TR>
$ACT_MES
</TBODY></TABLE>
</TR></TD></TABLE>

<form method=post action=./admin.cgi>
ID:<input type=text name=id size=7>
PASS:<input type=pass name=pass size=7>
<input type=submit value=�Ǘ���>
</form>

EOM

	&FOOTER;
	exit;

}
# _/_/_/_/_/_/_/_#
# ���ȃJ�E���^�[ #
# _/_/_/_/_/_/_/_#
sub COUNTER {

	$file_read = "$LOG_DIR/counter.cgi";
	open(IN,"$file_read") or &ERR2('�t�@�C�����J���܂���ł����B');
	@reading = <IN>;
	close(IN);

	($total_count) = split(/<>/,$reading[0]);
	$total_count++;

	&SAVE_DATA("$file_read","$total_count");
}
