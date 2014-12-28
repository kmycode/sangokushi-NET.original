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
require './ini_file/com_list.ini';
require 'suport.pl';

if($MENTE) { &ERR2("�����e�i���X���ł��B���΂炭���҂����������B"); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("�A�h���X�o�[�ɒl����͂��Ȃ��ł��������B"); }
if($mode eq 'STATUS') { &STATUS; }
else { &ERR("�s���ȃA�N�Z�X�ł��B"); }


#_/_/_/_/_/_/_/_/_/_/_/#
#_/  �X�e�[�^�X���  _/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub STATUS {

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&MAKE_GUEST_LIST;
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);
	if($kos ne 1){
		&ERR2("�F�؂��ς�ł��܂���B�o�^�������[���A�h���X�ɔF��ID���Y�t����Ă���̂œo�^���Ă��������B");
	}
	open(IN,"$LOG_DIR/date_count.cgi") or &ERR('�t�@�C�����J���܂���ł����B');
	@MONTH_DATA = <IN>;
	close(IN);

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$new_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);

	if($mmonth < 4){
		$bg_c = "#FFFFFF";
	}elsif($mmonth < 7){
		$bg_c = "#FFE0E0";
	}elsif($mmonth < 10){
		$bg_c = "#60AF60";
	}else{
		$bg_c = "#884422";
	}

	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
				$zsyo_sal += int($z2syo * 8 * $z2num / 10000);
				$znou_sal += int($z2nou * 8 * $z2num / 10000);
		}
	}
	if($xking eq "$kid"){
		$rank_mes = "�y�N��z";
	}elsif($xgunshi eq "$kid"){
		$rank_mes = "�y�R�t�z";
	}elsif($xdai eq "$kid"){
		$rank_mes = "�y�叫�R�z";
	}elsif($xuma eq "$kid"){
		$rank_mes = "�y�R�n���R�z";
	}elsif($xgoei eq "$kid"){
		$rank_mes = "�y��q���R�z";
	}elsif($xyumi eq "$kid"){
		$rank_mes = "�y�|���R�z";
	}elsif($xhei eq "$kid"){
		$rank_mes = "�y���R�z";
	}
	open(IN,"$UNIT_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@UNI_DATA = <IN>;
	close(IN);

	$uhit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){$uhit=1;last;}
	}
	if(!$uhit){
		$unit_id="";
		$uunit_name="������";
	}
	if($unit_id eq $kid){
		$add_com = "<option value=28>�W��";
	}
	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=green>��</font>$S_MOVE[$p]<BR>";$p++;}

	&TIME_DATA;

	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	$p=0;
	while($p<5){$log_list .= "<font color=navy>��</font>$LOG_DATA[$p]<BR>";$p++;}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$wyear = $myear+$F_YEAR;
	if($mtime > $kdate){
		$wmonth = $mmonth+1;
		if($wmonth > 12){
			$wyear++;
			$wmonth = 1;
		}
	}else{
		$wmonth = $mmonth;
	}

	for($i=0;$i<$MAX_COM;$i++){
		($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
		$no = $i+1;
		if($cid eq ""){
			$com_list .= "<TR><TH>[$wyear�N$wmonth��]</TH><TH> - </TH></TR>";
		}else{
			$com_list .= "<TR><TH>[$wyear�N$wmonth��]</TH><TH>$cname</TH></TR>";
		}
		$wmonth++;
		if($wmonth > 12){
			$wyear++;
			$wmonth = 1;
		}
	}

	open(IN,"$DEF_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@DEF_DATA = <IN>;
	close(IN);

	foreach(@DEF_DATA){
		($did,$dname,$dtown_id,$dtown_flg,$dcon)=split(/<>/);
		if($kpos eq $dtown_id){
			$def_list .= "$dname ";
		}
	}

	open(IN,"./charalog/main/$xking.cgi");
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename) = split(/<>/,$E_DATA[0]);
	$king_name=$ename;
	open(IN,"./charalog/main/$xgunshi.cgi");
	@S_DATA = <IN>;
	close(IN);
	($sid,$spass,$sname) = split(/<>/,$S_DATA[0]);
	$sub_name=$sname;

	$next_time = int(($kdate + $TIME_REMAKE - $tt) / 60);
	if($next_time < 0){
		$next_time = 0;
	}
	$del_out = $DEL_TURN - $ksub2;

	$dilect_mes = "";$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST") or &ERR('�t�@�C�����J���܂���ł����B');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon,$hunit) = split(/<>/);
		if($MES_MAN < $i && $MES_ALL < $h && $MES_COU < $j && $MES_UNI < $k) { last; }
		if(111 eq "$pid" && $kpos eq $hpos){
			if($MES_ALL < $h ) { next; }
			$all_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF><b>$hname\@$town_name[$hpos]����</b><BR>�u<b>$hmessage</b>�v<BR>$htime</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$h++;
		}elsif($kcon eq "$pid"){
			if($MES_COU < $j ) { next; }
			$cou_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=FFCC33><b>	$hname\@$town_name[$hpos]����$pname��</b></font><BR><font size=2 color=#FFFFFF>  �u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$j++;
		}elsif($kid eq "$pid"){
			if($MES_MAN < $i ) { next; }
			$add_mes = "<b><font color=orange>$hname\@$town_name[$hpos]</font>����$pname��</b> <BR>";
			$man_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF>$add_mes�u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$dilect_mes .= "<option value=\"$hid\">$hname�����";
			$i++;
		}elsif(333 eq "$pid" && "$hunit" eq "$unit_id" && "$hcon" eq "$kcon" && "$xcid" ne "0"){
			if($MES_UNI < $k ) { next; }
			$unit_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=orange><b>$kname����$pname��</b></font><BR><font size=2 color=#FFFFFF>  �u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$k++;
		}elsif($kid eq "$hid"){
			if($MES_MAN < $i ) { next; }
			$man_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=skyblue><b>$kname����$pname��</b></font><BR><font size=2 color=#FFFFFF>  �u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);

	$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST2") or &ERR('�t�@�C�����J���܂���ł����B');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($MES_MAN < $i) { last; }
		if($kid eq "$pid"){
			$add_mes="";
			$add_sel="";
			$add_form1="";
			$add_form2="";
			if($htime eq "9999"){
			$add_mes = "<B><font color=skyblue>$hname��$cou_name[$hcon]���ւ̎d�������߂Ă��܂��B</font><BR></B>";
			$add_sel = "<BR><input type=radio name=sel value=1>��������<input type=radio name=sel value=0>�f��<input type=submit value=\"�Ԏ�\">";
			$add_form1="<form action=\"./mydata.cgi\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=hcon value=$hcon><input type=hidden name=hid value=$hid><input type=hidden name=hpos value=$hpos><input type=hidden name=mode value=COU_CHANGE>";
			$add_form2="</form>";
			}else{
			$add_mes = "<B><font color=skyblue>$hname����$pname��</font><BR></B>";
			}
			$man_mes2 .= "$add_form1<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF>$add_mes�u<b>$hmessage</b>�v$add_sel</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>$add_form2\n";
			$dilect_mes .= "<option value=\"$hid\">$hname�����";
			$i++;
		}elsif($kid eq "$hid"){
			$man_mes2 .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=skyblue><b>$kname���񂩂�$pname��</b></font><BR><font size=2 color=#FFFFFF>  �u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);

	if($xking eq $kid || $xgunshi eq $kid){
		$king_com = "<form action=\"./mydata.cgi\" method=\"post\"><TR><TH colspan=8><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM><input type=submit value=\"�w�ߕ�\"></TH></TR></form>";
		foreach(@COU_DATA){
			($xvcid,$xvname)=split(/<>/);
			$dilect_mes .= "<option value=\"$xvcid\">$xvname����";
		}
	}

	if($xmark < $BATTLE_STOP){
		$xc = $BATTLE_STOP - $xmark;
		$xaddmes = "<BR>�퓬�����܂Ŏc�� <font color=red>$xc</font> �^�[��";
	}

	$klank = int($kclass / $LANK);
	if($klank > 20){
		$klank=20;
	}

	$nou_bar1 = int($znou/$znou_max*100);
	$nou_bar2 = 100 - $nou_bar1;
	$syo_bar1 = int($zsyo/$zsyo_max*100);
	$syo_bar2 = 100 - $syo_bar1;
	$tec_bar1 = int($zsub1/999*100);
	$tec_bar2 = 100 - $tec_bar1;
	$shiro_bar1 = int($zshiro/$zshiro_max*100);
	$shiro_bar2 = 100 - $shiro_bar1;
	$Tshiro_bar1 = int($zdef_att/999*100);
	$Tshiro_bar2 = 100 - $Tshiro_bar1;

	&HEADER;
print <<"EOM";
<TABLE border=0 width=100% height=100%><TR><TD>
[<a href=$BBS1_URL>$BBS1</a>]
<TABLE border=0 width=100%>
<TR><TD bgcolor=$ELE_BG[$cou_ele[$zcon]] colspan=2><font color=$ELE_C[$cou_ele[$zcon]] size=2>$xname���w��:$xmes</font></TD></TR><TR><TD width=50%>
<TABLE width=100%><TR><TD width=50%>
<font color=AA8866><B>- �嗤�n�} -</B></font>
<TABLE bgcolor=$bg_c width=100% height=5 border="0" cellspacing=1><TBODY>
<TR><TH colspan= 11 bgcolor=442200><font color=FFFFFF>$new_date</TH></TR>
          <TR>
            <TD width=20 bgcolor=$TD_C2>-</TD>
EOM
    for($i=1;$i<11;$i++){
		print "<TD width=20 bgcolor=$TD_C1>$i</TD>";
	}
	print "</TR>";
     for($i=0;$i<10;$i++){
		$n = $i+1;
		print "<TR><TD bgcolor=$TD_C3>$n</td>";
		for($j=0;$j<10;$j++){
				$m_hit=0;$zx=0;
				foreach(@TOWN_DATA){
					($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy)=split(/<>/);
					if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
					$zx++;
				}
				$col="";
				if($m_hit){
					if($zx eq $kpos){
						$col = $ELE_C[$cou_ele[$zzcon]];
					}else{
						$col = $ELE_BG[$cou_ele[$zzcon]];
					}
					if($zzname eq "���z" || $zzname eq "����" || $zzname eq "���s" || $zzname eq "��" ){
						print "<TH bgcolor=$col><img src=\"$IMG/m_1.gif\" title=\"$zzname�y$cou_name[$zzcon]�z\"></TH>";
					}else{
						print "<TH bgcolor=$col><img src=\"$IMG/m_4.gif\" title=\"$zzname�y$cou_name[$zzcon]�z\"></TH>";
					}
				}else{
					print "<TH> </TH>";
				}
		}
		print "</TR>";
	}
print <<"EOM";
</TBODY></TABLE>
</TD></TR>
<TR><TD>

<TABLE width=100% bgcolor=$ELE_BG[$cou_ele[$zcon]] cellspacing=2><TBODY bgcolor=$ELE_C[$cou_ele[$zcon]]>
<TR><TH bgcolor=$ELE_BG[$xele] colspan=2><font color=$ELE_C[$xele]>$zname</font></TH></TR>
<TR><TD>�x�z��</TD><TH bgcolor$TD_C1>$cou_name[$zcon]��</Th></TR>
<TR><TD>�_��</TD><TD align=right>$znum</TD></TR>
<TR><TD>����</TD><TD align=right>$zpri</TD></TR>
<TR><TD>�_��</TD><TD align=right NOWRAP><img src=$IMG/img/bar1.gif width=$nou_bar1\% height=5><img src=$IMG/img/bar2.gif width=$nou_bar2\% height=5><BR>$znou/$znou_max</TD></TR>
<TR><TD>����</TD><TD align=right NOWRAP><img src=$IMG/img/bar1.gif width=$syo_bar1\% height=5><img src=$IMG/img/bar2.gif width=$syo_bar2\% height=5><BR>$zsyo/$zsyo_max</TD></TR>
<TR><TD>�Z�p��</TD><TD align=right NOWRAP><img src=$IMG/img/bar1.gif width=$tec_bar1\% height=5><img src=$IMG/img/bar2.gif width=$tec_bar2\% height=5><BR>$zsub1/999</TD></TR>
<TR><TD>���</TD><TD align=right NOWRAP><img src=$IMG/img/bar1.gif width=$shiro_bar1\% height=5><img src=$IMG/img/bar2.gif width=$shiro_bar2\% height=5><BR>$zshiro/$zshiro_max</TD></TR>
<TR><TD>��Ǒϋv��</TD><TD align=right NOWRAP><img src=$IMG/img/bar1.gif width=$Tshiro_bar1\% height=5><img src=$IMG/img/bar2.gif width=$Tshiro_bar2\% height=5><BR>$zdef_att/999</TD></TR>
</TBODY></TABLE>

<TABLE width=100% bgcolor=$ELE_BG[$cou_ele[$zcon]] cellspacing=1><TBODY bgcolor=$ELE_C[$cou_ele[$zcon]]>
<TR><TD>Online</TD><TD>$m_list</TD></TR>
</TBODY></TABLE>

</TD></TR><TR><TD>
<TABLE width=100% bgcolor=$ELE_BG[$xele] cellspacing=1><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH bgcolor=$ELE_BG[$xele] colspan=8><font color=$ELE_C[$xele]>$xname��$xaddmes</font></TH></TR>
<TR><TD>�N��</TD><TH colspan=2>$king_name</TH><TD>�R�t</TD><TH colspan=2>$sub_name</TH></TR>
<TD>�x�z�s�s</TD><TD align=right>$town_get[$kcon]</TD><TD>���n</TD><TD align=right>$znou_sal</TD>
<TD>�ŋ�</TD><TD align=right>$zsyo_sal</TD></TR>

<form action="./mydata.cgi" method="post"><TR><TH colspan=3>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=COUNTRY_TALK>
<input type=submit value="��c��">
</TH></form>
<form action="./mydata.cgi" method="post"><TH colspan=3>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="���@">
</TH></TR></form>
$king_com
</TBODY></TABLE>
</TD></TR>
<TR><TD>

<form action="./command.cgi" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<TABLE bgcolor=$ELE_BG[$xele] cellspacing=1><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>�R�}���h</font></TH></TR>
<TR><TD>
No:<select name=no size=4 MULTIPLE>
<option value="all">ALL
EOM
	for($i=0;$i<$MAX_COM;$i++){
		$no = $i+1;
		if($i eq "0"){
		print "<option value=\"$i\" SELECTED>$no";
		}else{
		print "<option value=\"$i\">$no";
		}
	}

print <<"EOM";
</select>

<select name=mode>
<option value=$NONE>�������Ȃ�
<option value="">== ���� ==
<option value=$NOUGYOU>�_�ƊJ��(50G)
<option value=$SYOUGYOU>���Ɣ��W(50G)
<option value=$TEC>�Z�p�J��(50G)
<option value=$SHIRO>��ǋ���(50G)
<option value=$SHIRO_TAI>��Ǒϋv�͋���(50G)
<option value=$RICE_GIVE>�Ď{��(50R)
<option value="">== �R�� ==
<option value=$GET_SOL>����
<option value=$KUNREN>���m�P��
<option value=$TOWN_DEF>��̎��
<option value=$BATTLE>�푈
<option value="">== ���� ==
<option value=$GET_MAN>�o�p(100G)
<option value="">== �b�B ==
<option value=$TANREN>\�\\�͋���(50G)
<option value="">== ���l ==
<option value=$BUY>�Ĕ���
<option value=$ARM_BUY>����w��
<option value=$DEF_BUY>�����w��
<option value="">== �ړ� ==
<option value=$MOVE>�ړ�
$add_com
<option value=$SHIKAN>�d��
</select><input type=submit value=\"���s\">
<BR>��No��ctrl�L�[�������Ȃ���N���b�N����ƕ����I���ł��܂��B
</TD></form></TR>
<TR><TH>���̃^�[���܂�$next_time��</TH></TR>
<TR><TH>���u�폜�^�[���܂�<font color=red>$del_out</font>�^�[��</TH></TR>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<TR><TH><input type=submit value="���RELODE">
</TH></TR></form>
</TBODY></TABLE><CENTER>
</TD></TR>
</TABLE>

</TD><TD width=100%>

<TABLE width=100%><TR><TD width=100%>
<TABLE width=100% bgcolor=$TABLE_C cellspacing=1><TBODY BGCOLOR=$TD_C2>
<TR><TH bgcolor=#000000 colspan=2><font color=#FFFFFF>�R�}���h���X�g</font></TH></TR>
$com_list
</TABLE>

</TD></TR>
<TR><TD>

<TABLE width=100% bgcolor=$ELE_BG[$xele] cellspacing=1><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname$rank_mes</font></TH></TR>

<TR><TD rowspan=4 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>�m��</TD><TH>$kint</TH><TD>������</TD><TH>$klea</TH></TR>
<TR><TD>��EX</TD><TH>$kstr_ex</TH><TD>�mEX</TD><TH>$kint_ex</TH><TD>��EX</TD><TH>$klea_ex</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�l�]</TD><TH>$kcha</TH></TR>
<TR><TD>�K��</TD><TH>$LANK[$klank]</TH><TD>�v��</TD><TH>$kcex</TH><TD>�K���l</TD><TH>$kclass</TH></TR>
<TR><TD>������</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>����</TD><TH colspan=3>$uunit_name</TH></TR>
<TR><TD>����</TD><TH colspan=2>$SOL_TYPE[$ksub1_ex]</TH><TD>���m</TD><TH>$ksol</TH><TD>�P��</TD><TH>$kgat</TH></TR>
<TR><TD>����</TD><TH colspan=5>$karmname</TH><TH>$karmdmg</TH></TR>
<TR><TD>����</TD><TH colspan=5>$kproname</TH><TH>$kprodmg</TH></TR>
<form action="./mydata.cgi" method="post"><TR><TD>�����x</TD><TH>$kbank</TH><TH colspan=5>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=CYUUSEI>
<input type=text name=cyuu size=5>
<input type=submit value="����">
</TH></TR></form>
<form action="./mydata.cgi" method="post"><TR><TH colspan=7>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<select name=mode>
<option value=LETTER>�l���Ď莆
<option value=UNIT_SELECT>�����Ґ�
<input type=submit value="���s">

</TH></TR></form>
</TBODY></TABLE>

</TD></TR>
</TABLE>
</TD></TR>

<TR><TD colspan=2>
<TABLE width=100% bgcolor=$ELE_BG[$cou_ele[$zcon]] cellspacing=1><TR><TD bgcolor=$ELE_C[$cou_ele[$zcon]]><font color=$ELE_BG[$cou_ele[$zcon]]>$zname�̎��:$def_list</TD></TR></TABLE>
</TD></TR>
<TR><TD colspan=2>
<TABLE width=100% bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C1>$S_MES</TD></TR></TABLE>
<form action="$FILE_MYDATA" method="post">
�莆�F<input type="text" name=message size=60>
 <select name=mes_id><option value="$xcid">$xname����<option value="111">$zname�̐l��<option value="333">$uunit_name�����̐l��$dilect_mes</select>
 <input type=hidden name=id value=$kid>
 <input type=hidden name=name value=$kname>
 <input type=hidden name=pass value=$kpass>
 <input type=hidden name=mode value=MES_SEND>
 <input type=submit value="���M"></form>
<TABLE width=100%><TBODY>
<TR><TD width=50%>
	$zname�̐l�X��:($MES_ALL��)
	<TABLE width=100% bgcolor=880000><TBODY>
	$all_mes
	</TBODY></TABLE>

	$kname����:($MES_MAN��)
	<TABLE width=100% bgcolor=008800><TBODY>
	$man_mes
	</TBODY></TABLE>

	$kname���Ė���:($MES_MAN��)
	<TABLE width=100% bgcolor=008800><TBODY>
	$man_mes2
	</TBODY></TABLE>
</TD><TD>
	$xname������:($MES_COU��)
	<TABLE width=100% bgcolor=000088><TBODY>
	$cou_mes
	</TBODY></TABLE>

	$uunit_name��������:($MES_UNI��)
	<TABLE width=100% bgcolor=AA8833><TBODY>
	$unit_mes
	</TBODY></TABLE>

</TD></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD colspan=2>
<TABLE width=100% bgcolor=$ELE_BG[$cou_ele[$kcon]]><TR><TD colspan=2 bgcolor=$ELE_C[$cou_ele[$kcon]]>$log_list</TD></TR><form action="./mylog.cgi" method="post">
<TR><TD bgcolor=$ELE_C[$cou_ele[$kcon]]><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=submit value="�s�s���"></TD></form><form action="./mycou.cgi" method="post">
<TD bgcolor=$ELE_C[$cou_ele[$kcon]]><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value="���f�[�^">
</TD></TR>
</TABLE></form>

</TD></TR>
</TABLE>
</TD></TR></TABLE>
EOM
	&FOOTER;
	exit;
}

