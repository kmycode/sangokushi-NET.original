#_/_/_/_/_/_/_/_/_/#
#_/    �����z��  _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_SELECT {

	&CHARA_MAIN_OPEN;

	open(IN,"$TOWN_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@TOWN_DATA = <IN>;
	close(IN);
	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes)=split(/<>/);
		if("$zcid" eq "$in{town}"){last;}
	}


	open(IN,"$UNIT_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@UNI_DATA = <IN>;
	close(IN);

	@UNI_DATA2 = @UNI_DATA;
	$i=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$ucon" eq "$kcon" && $ureader){

			$unit_num=1;
			$unit_list = "$uname";

			if($uid eq $kid){
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",$uname2";
						$unit_num++;
						$u_member .= "<option value=$uid2>$uname2";
					}
				}

			}else{
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",$uname2";
						$unit_num++;
					}
				}
			}
			if($uflg eq "1"){
				$u_mes = "��������";
			}else{
				$u_mes = "�����n�j";
			}
			$unit_party .= "<TR><TD bgcolor=$TD_C3><input type=radio name=unit_id value=$unit_id></TD><TD bgcolor=$TD_C2><img src=\"$IMG/$uchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$uname\"></TD><TD bgcolor=$TD_C1><font size=1>$uunit_name����<BR>($uname)</TD><td bgcolor=$TD_C1>$unit_list</td><td bgcolor=$TD_C2>$unit_num�l</td><td bgcolor=$TD_C2>$umes</td><TD bgcolor=$TD_C1>$u_mes</TD></tr>";
		}

		if($uid eq $kid){
			$k_hit=1;
			$kunit_name = $uunit_name;
		}
	}

	if(!$k_hit){
		$kunit_name = "������";
	}

	&HEADER;

	print <<"EOM";
<table width="100%" cellpadding="0" cellspacing="0" border=0><tr><td>
<TABLE WIDTH="100%" border=0>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$kele] WIDTH=100% height=5>�@<font color=$ELE_C[$kele] size=4>�@�@�@����<B> * �� �� �z �� �E �� ��*</B>����</font></TD>
</TR><TR>
<TD bgcolor=$TD_C4 height=5>
<TABLE border="0"><TBODY>
<TR>
<TD bgcolor=$TD_C1><img src="$IMG/$kchara.gif" width="$img_wid" height="$img_height" alt="$kname"></TD>
<TD bgcolor=$TD_C2>$simg</TD>
<TD bgcolor=$TD_C3>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center>
<table cellpadding="0" cellspacing="0" border=0><tr><td bgcolor=$TABLE_C>
<TABLE border="0" cellspacing="2">
<TBODY>
<TR>
<TD bgcolor=$TD_C2>���O</TD>
<TD bgcolor=$TD_C3>�k�u</TD>
<TD bgcolor=$TD_C2>����</TD>
<TD bgcolor=$TD_C3>�E��</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>$kname</TD>
<TD bgcolor=$TD_C3 align=right>$klv</TD>
<TD bgcolor=$TD_C2>$ELE[$kele]��</TD>
<TD bgcolor=$TD_C3>$SYOKU[$kclass]</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>������</TD>
<TD bgcolor=$TD_C1 colspan=3 align=right>$kgold GOLD</TD>
</TR>
</TBODY></TABLE>
</td></tr></table>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD width="100%" bgcolor=$TALK_BG><font color=$TALK_FONT>�����ł͎����̏������镔���ɔz�����鎖���o���܂��B<BR>���Ȃ��͌���<font color=red>$kunit_name</font>�����ɏ������Ă��܂��B<BR>�����ɏ�������ƕ����`���b�g��W���R�}���h�œ��������₷���Ȃ�܂��B</font></TD>
<TD bgcolor=$TD_C4></TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD><BR><BR>
<form action="$FILE_MYDATA" method="post">
<CENTER><TABLE bgcolor=$TABLE_C><TBODY><TR>
<TD bgcolor=$TD_C3>�I��</TD><TD bgcolor=$TD_C2>����</TD><TD bgcolor=$TD_C1>������(����)</TD><TD bgcolor=$TD_C1>�z������</TD><TD bgcolor=$TD_C1>������</TD><TD bgcolor=$TD_C2>������W���b�Z�[�W</TD><TD bgcolor=$TD_C1>������t</TD></TR>
EOM


print <<"EOM";
$unit_party
</TR></TBODY></TABLE></CENTER>

<BR>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_ENTRY>
<input type=submit value="����"></form>
<HR size=0>
<h3><font color=3355AA><b>�������R�}���h</B></font></h3>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_CHANGE>
<input type=submit value="�������ہE����"></form>
�����s����Ƒ��̐l�͂��̕����ɓ����o���Ȃ��Ȃ�܂��B<p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<select name=did>$u_member</select>
<input type=hidden name=mode value=UNIT_OUT>
<input type=submit value="��������"></form>
�����s����Ƃ��̕����͑ދ��������܂��B<p>


<HR size=0>

<b class=\"clit\">�V�K�����쐬</B></font>�i�K���l �T�O�O�ȏ�K�v�j
<form action="$FILE_MYDATA" method="post">
<TABLE bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C3>������</TD><TD bgcolor=$TD_C2><input type=text name=name size=30><BR>[�S�p�啶���łQ�`�W�����ȓ�]</TD></TR>
<TD bgcolor=$TD_C3>������W�̃R�����g</TD><TD bgcolor=$TD_C2><input type=text name=mes size=30><BR>[�S�p�啶���łO�`�Q�O�����ȓ�]</TD>
</TABLE>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=MAKE_UNIT>
<input type=submit value="�����쐬"></form>
<HR size=0>
<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_DELETE>
<input type=submit value="�����E�ށE���U"></form>
<HR size=0>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�X�ɖ߂�"></form>
</TD>
</TR>
</TBODY></TABLE>
</td></tr></table>
EOM

	&FOOTER;
	exit;
}
1;