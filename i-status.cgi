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
require 'i-suport.pl';

if($MENTE) { &ERR2("�����e�i���X���ł��B���΂炭���҂����������B"); }
&DECODE;
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
	for($i=0;$i<$MAX_COM;$i++){
		($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
		$no = $i+1;
		if($cid eq ""){
		$com_list .= "$no: - <BR>";
		}else{
		$com_list .= "$no: $cname<BR>";
		}
	}

	open(IN,"$DEF_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@DEF_DATA = <IN>;
	close(IN);

	foreach(@DEF_DATA){
		($did,$dname,$dtown_id,$dtown_flg,$dcon)=split(/<>/);
		if($kpos eq $dtown_id){
			$def_list .= "$dname,";
		}
	}
	chop($def_list);
	$next_time = int(($kdate + $TIME_REMAKE - $tt) / 60);
	if($next_time < 0){
		$next_time = 0;
	}
	$del_out = $DEL_TURN - $ksub2;

	$dilect_mes = "";$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST") or &ERR('�t�@�C�����J���܂���ł����B');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($MES_MAN < $i && $MES_ALL < $h) { last; }
		if(111 eq "$pid" && $kpos eq $hpos){
			if($MES_ALL < $h ) { next; }
			$all_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF><b>$hname����</b><BR>�u<b>$hmessage</b>�v<BR>$htime</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$h++;
		}elsif($kid eq "$pid"){
			if($MES_MAN < $i ) { next; }
			$man_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF><b><font color=orange>$hname</font>����$pname��</b> <BR>�u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$dilect_mes .= "<option value=\"$hid\">$hname�����";
			$i++;
		}elsif($kid eq "$hid"){
			if($MES_MAN < $i ) { next; }
			$man_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=skyblue><b>$kname���񂩂�$pname��</b></font><BR><font size=2 color=#FFFFFF>  �u<b>$hmessage</b>�v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);
	$klank = int($kclass / $LANK);
	if($klank > 20){
		$klank=20;
	}
	&HEADER;
print <<"EOM";
�w��:$xmes<HR>
$new_date<BR><BR>
<B>\[$zname\]</B><BR>
�x�z��:$cou_name[$zcon]��<BR>
�_��:$znum�l | ����:$zpri<BR>
�_��:$znou/$znou_max<BR>
����:$zsyo/$zsyo_max<BR>
�Z�p:$zsub1/999<BR>
���:$zshiro/$zshiro_max<BR>
��Ǒϋv��:$zdef_att/999<BR>
����:$zsouba
<BR>
<B>\[�R�}���h���X�g\]</B><BR>
<HR>$com_list<HR>
<form action="./i-command.cgi" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<B>\[�R�}���h\]</B><BR>
No:<select name=no size=4 MULTIPLE>
<option value=all>ALL
EOM
	for($i=0;$i<$MAX_COM;$i++){
		$no = $i+1;
		print "<option value=\"$i\">$no";
	}
print <<"EOM";
</select>
<select name=mode>
<option value="0">�������Ȃ�
<option value="">== ���� ==
<option value="1">�_�ƊJ��(50G)
<option value="2">���Ɣ��W(50G)
<option value="29">�Z�p�J��(50G)
<option value="3">��ǋ���(50G)
<option value="30">��Ǒϋv�͋���(50G)
<option value="8">�Ď{��(50R)
<option value="">== �R�� ==
<option value="9">����
<option value="11">���m�P��
<option value="12">��̎��
<option value="13">�푈
<option value="">== ���� ==
<option value="24">�o�p(100G)
<option value="">== �b�B ==
<option value="26">\�\\�͋���(50G)
<option value="">== ���l ==
<option value="14">�Ĕ���
<option value="15">����w��
<option value="16">�����w��
<option value="">== �ړ� ==
<option value="17">�ړ�
<option value="21">�d��
$add_com
</select><input type=submit value=\"���s\"></form>
���̃^�[���܂�$next_time��<BR><BR>
$kname\[$uunit_name����\]<BR>
��:$kgold/��:$krice:�v��:$kcex<BR>
<p>
$zname�̎��:$def_list<BR>
$log_list
<form action="./i-command.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=mode value=COUNTRY_TALK>
<input type=hidden name=pass value=$kpass>
<input type=submit value="��c��">
</form>

<form action="./i-mylog.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value="�ߋ����O">
</TD></TR></form>
</TABLE>
</TD></TR></TABLE>
EOM
	&FOOTER;
	exit;
}

