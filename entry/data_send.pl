#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/     NEW CHARA DATA �쐬    _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub DATA_SEND {

	open(IN,"$TOWN_LIST") or &ERR2("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@TOWN = <IN>;
	close(IN);

	&CHARA_MAIN_OPEN;
	&HEADER;

	print <<"EOM";
<CENTER><h3>�����o�^��������</h3>
<hr size=0>
$kname��$GAME_TITLE�̐��E�ɓo�^����܂����B<BR>ID��PASS��Y��Ȃ��悤�Ƀ������Ēu���ĉ������B
<hr size=0>
ID�F<font color=red>$in{'id'}</font><BR>
PASS �F<font color=red>$in{'pass'}</font><BR>
<p>
�X�e�[�^�X<BR><table border=0 bgcolor=$TABLE_C cellspacing=1><TBODY bgcolor=$TD_C4>
<tr><td rowspan="8" align="center"><img src="$IMG/$in{'chara'}.gif"></td>
<td class="b1">���O</td><td>$in{'chara_name'}</td>
<td class="b1">��</td><td>$cou_name</td></tr>
<tr><td class="b1">�K��</td><td>$LANK[0]</td>
<td class="b1">�����ʒu</td><td>$z2name</td></tr>
<tr><td class="b1">����</td><td>$in{'str'}</td>
<td class="b1">�m��</td><td>$in{'int'}</td></tr>
<tr><td>������</td><td>$in{'tou'}</td>
<td>mail</td><td>$in{'mail'}</td></tr>
</table><p>
���S�Ҍ���<form action="$FILE_ENTRY" method="post">
<input type="hidden" name=mode value=RESISDENTS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=num value="0">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="�Q�[���̐���">
</form><p>
�o���Ҍ���<form action="$FILE_STATUS" method="post">
<input type="hidden" name=mode value=STATUS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="�Q�[�����J�n">
</form></CENTER>
EOM

		&FOOTER;

		exit;
}
1;