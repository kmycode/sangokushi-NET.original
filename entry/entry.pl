#_/_/_/_/_/_/_/_/_/#
#_/   �V�K�o�^   _/#
#_/_/_/_/_/_/_/_/_/#

sub ENTRY {

	&CHEACKER;
	&HEADER;

	open(IN,"$COUNTRY_MES") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@MES_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('�t�@�C�����J���܂���ł����Berr no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}

	$mess .= "<TR><TD BGCOLOR=$TD_C1 colspan=2>�e���̐V�K�Q���҂ւ̃��b�Z�[�W</TD></TR>";
	foreach(@MES_DATA){
		($cmes,$cid)=split(/<>/);
		$mess .= "<TR><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cou_name[$cid]��</TD><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cmes</TD></TR>";
	}



	open(IN,"$TOWN_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@TOWN_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$t_list .= "<option value=\"$zc\">$z2name�y$cou_name[$z2con]�z";
		$zc++;
	}
	if($in{'url'} eq ""){$nurl = "http://";}else{$nurl = "$in{'url'}";}
	if($in{'mail'} eq ""){$nmail = "\@";}else{$nmail = "$in{'mail'}";}
	if(ATTESTATION){$emes = "�E<font color=red>�F��ID�t���̊m�F���[���𑗂�܂��̂Ő��������͂��Ă��������B</font><BR>(�����̃��[���A�h���X�̓Q�[�����ł̂ݎg�p���܂��B�X�p�����[���₻�̑��ւ̗��p�͈�؂��܂���B)";}
	print <<"EOM";
	<script language="JavaScript">
		function changeImg(){
			num=document.para.chara.selectedIndex;
			document.Img.src="$IMG/"+ num +".gif";
		}
	</script>
<hr size=0><CENTER><font size=4><b>-- �����o�^ --</b></font><hr size=0><form action="$FILE_ENTRY" method="post" name=para><input type="hidden" name="mode" value="NEW_CHARA">
<table bgcolor=$TABLE_C width=80% border=0 cellpadding="1" cellspacing="1">$mess</table>

<table bgcolor=$TABLE_C border=0 cellpadding="3" cellspacong="1"><tr><TD colspan=2 bgcolor=$TD_C1>
* ID��PASS�������ꍇ�o�^�o���܂���B<BR>
* �Q�d�o�^�͏o���܂���<BR>
* �ő�o�^�l����$ENTRY_MAX���ł��B�i���ݓo�^��$num���j<BR>
* ���ׂĂ̍��ڂ��L�����Ă��������B<BR>
* <a href="./manual.html" TARGET="_blank">�Q�[������</a>���悭�ǂ�ł���Q�����Ă��������B<BR>
* ���[���A�h���X�͐��������͂��Ă��������B�o�^���ꂽ���[���A�h���X�ɔF��ID�𑗐M���܂��B�m�F���Ƃꂽ���_�ŎQ������\�\\�ɂȂ�܂��B�ihotmail yahoomail�̎g�p�s�j<BR>
*�����ʒu�ɉ����̎x�z�������Ă��Ȃ��s�s�i�y�z�󗓂̓s�s�j��I������ƌN��Ƃ��ĎQ��\��\�\\�ł��B����ȊO�͂��̊X�̏��L�҂̔z���ɂȂ�܂��B<a href="./ranking.cgi" TARGET="_blank">�X�ꗗ</a> <BR>
</TD></tr><tr bgcolor=$TD_C2><TD width=100>�� �O</tD><tD bgcolor=$TD_C3><input type="text" name="chara_name" size="30" value="$in{'chara_name'}"><br>�E�����̖��O����͂��Ă��������B<BR>[�S�p�啶���łQ�`�U�����ȓ�]</tD></tr><tr><TD bgcolor=$TD_C2>�C���[�W</TD><TD bgcolor=$TD_C3><TABLE bgcolor=$TABLE_C border=2><TR><TD><img src=\"$IMG/0.gif\" name=\"Img\">
</TD></TR></TABLE><select name=chara onChange=\"changeImg()\">
EOM
	foreach (0..$CHARA_IMAGE){print "<option value=\"$_\">�C���[�W[$_]\n";}
	print <<"EOM";
</select><br>�E�����̃C���[�W��I��ł��������B</TH></tr>

<tr bgcolor=$TD_C2><TD>�����ʒu</TD><TD bgcolor=$TD_C3><select name="con">
<option value=""> �I�����Ă�������
$t_list
</select><br>�E�������鍑��I��ł��������B�i�y�z�͌�����\�\\)</TD></tr><tr><TD bgcolor=$TD_C2>ID</TD><TD bgcolor=$TD_C3><input type="text" name="id" size="10" value="$in{'id'}"><br>�E�Q�������]ID���L�����Ă��������B<BR>[���p�p�����łS�`�W�����ȓ�]</TD></tr><tr><TD bgcolor=$TD_C2>�p�X���[�h</TD><TD bgcolor=$TD_C3><input type="password" name="pass" size="10"  value="$in{'pass'}"><br>�E�p�X���[�h��o�^���Ă��������B<BR>[���p�p�����łS�`�W�����ȓ�]</TD></tr>
<tr><TD bgcolor=$TD_C2>\�\\��</TD><TD bgcolor=$TD_C3><table><TR><TD>����</TD><TD><input type="text" name="str" size="5">[5�`100]</TD></TR><TR><TD>�m��</TD><TD><input type="text" name="int" size="5">[5�`100]</TD></TR><TR><TD>������</TD><TD><input type="text" name="tou" size="5">[5�`100]</TD></TR></TABLE>�E\�\\�͂��w�肵�ĉ������B�B<BR>[�S���̍��v��150�ɂȂ�悤�ɂ��ĉ������B]</TD></tr>

<tr><TD bgcolor=$TD_C2>���[���A�h���X</TD><TD bgcolor=$TD_C3><input type="text" name="mail" size="35" value="$nmail"><br> $emes</TD></tr>
</table>
<BR>
<TABLE width=80% bgcolor=$TABLE_C>
<tr><TH bgcolor=$TD_C3 colspan=2>�N��</TH></TR>
<tr><TD bgcolor=$TD_C1 colspan=2>
�E�����ʒu��*�����Ă���ꍇ�͂�������o�^���Ă��������B
</TD></TR>
<tr bgcolor=$TD_C1><TD width=100>����</tD><tD bgcolor=$TD_C3><input type="text" name="cou_name" size="30" value="$in{'cou_name'}"><br>�E�V���Ƃ̖��̂����߂Ă��������B<BR>[�S�p�啶���łP�`�S�����ȓ�]</tD></tr>
<tr><TD bgcolor=$TD_C1>���F</TD><TD bgcolor=$TD_C3>
EOM
	$i=0;
	foreach(@ELE_BG){print "<input type=radio name=ele value=\"$i\"><font color=$ELE_BG[$i]>��</font> \n";$i++;}
	print <<"EOM";
<br>�E���̐F�����߂Ă��������B</TD></tr>
</TABLE>

</table>
</td></tr>
<tr><TH align="center" bgcolor=$TABLE_C><input type="submit" value="�o�^"></TH></tr></table></form></CENTER>

EOM

	# �t�b�^�[�\��
	&FOOTER;

	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/   �Q���o�^�ҏ���`�F�b�N   _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("�t�@�C���I�[�v���G���[�I");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("�ő�o�^��\[$ENTRY_MAX\]�𒴂��Ă��܂��B���ݐV�K�o�^�o���܂���B");
		}
	}
}
1;