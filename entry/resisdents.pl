#_/_/_/_/_/_/_/_/_/#
#_/     �� ��    _/#
#_/_/_/_/_/_/_/_/_/#

sub RESISDENTS {

	&CHARA_MAIN_OPEN;

# �Q�[�����J�n���鎞�Ɏn�܂����
$P_MES[0] = "�O���uNET�̐��E�ւ悤�����I<br>�����ł͊�{�I�ȃQ�[���̗���ƃv���C���[�̖ړI�ɂ��Đ������Ă����܂��ˁB";
$P_MES[1] = "�܂��A�����Ɏ��s���������R�}���h����͂��Ă����܂��B<BR>�ő�łQ�O�܂Ŏw�߂��o�����Ƃ�\��\�\\�ł��B";
$P_MES[2] = "���̃Q�[���͂Q���Ԃ��ƂɍX�V���Ă����܂��B<BR>2���Ԃ��Ǝ��̃^�[���֐i�݂܂��B";
$P_MES[3] = "�^�[�����i�ނƕ����͎��̍s�����N�����܂��B<BR>�s�����~�܂�Ȃ��悤�ɐ��ǂ�Ŏ��ւƖ��߂��o���Ă����Ă��������B";
$P_MES[4] = "����Ȃ������͓����R�}���h�����s����Ƃ������Ǝv���܂��B<BR>�����ɂ͏��ƂƔ_�n�Ə邪����܂��B";
$P_MES[5] = "�_�n�͂V���̕Ă̎��n�ɁA���Ƃ͂P���̋��̎����ɉe�����Ă��܂��B<BR>�����ɗאڂ��Ă��čU�߂�ꂻ���ȏꍇ�͍ŏ��ɏ����������̂���ł��B";
$P_MES[6] = "�����ł�����x�����Ă����瑼���֐푈���܂��傤�B<BR>�P�ƂōU�߂���������̐l�Ƒ��k���čU�ߍ��񂾂ق������Ƃ��₷���ł��B";
$P_MES[7] = "����ł͑����v���C���Ă݂܂��傤�I";
	&HEADER;

	print <<"EOM";
<TABLE WIDTH="100%" height=100%>
<TBODY><TR>
<TD WIDTH=100% height=5>�@<font size=4>�@�@�@����<B> * �Q�[���̐��� *</B>����</font></TD>
</TR><TR>
<TD bgcolor=$TD_C4 height=5>
<TABLE border="0"><TBODY>
<TR>
<TD bgcolor=$TD_C1><img src="$IMG/$kchara.gif"></TD>
<TD bgcolor=$TD_C2>$simg</TD>
<TD bgcolor=$TD_C3>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center>
<TABLE bgcolor=$TABLE_C border="0">
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
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD bgcolor=$TD_C4><img src="$IMG/wiz.gif" title="�Z���t"></TD><TD width="100%" height=100 bgcolor=$TALK_BG><font size=3 color=$TALK_FONT>$P_MES[$in{'num'}]</font></TD>

</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD>
EOM
	$new_num = $in{'num'}+1;
if($new_num < @P_MES){
print "<form action=\"$FILE_ENTRY\" method=\"post\">
<input type=hidden name=id value=$kid>
<input type=hidden name=num value=$new_num>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=RESISDENTS>
<input type=submit value=\"����\"></form>";
}
print<<"EOM";
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�Q�[�����n�߂�"></form>

</TD>
</TR>
</TBODY></TABLE>
EOM

	&FOOTER;
	exit;
}
1;