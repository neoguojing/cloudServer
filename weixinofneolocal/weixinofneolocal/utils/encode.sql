alter table interface_weixinusers convert to character set utf8;
alter table interface_weixingroups convert to character set utf8;
alter table  interface_weixindeveloperinfo convert to character set utf8;
alter table interface_videomsg convert to character set utf8;
alter table interface_textmsg convert to character set utf8;
alter table interface_news convert to character set utf8;
alter table interface_musicmsg convert to character set utf8;
alter table interface_mediamsg convert to character set utf8;
alter table interface_itemofnews convert to character set utf8;
alter table django_admin_log convert to character set utf8;
alter table interface_locationofuser convert to character set utf8;
alter table interface_msgrecord convert to character set utf8;
alter table auth_group convert to character set utf8;


ALTER TABLE `interface_weixinusers` DROP PRIMARY KEY, ADD PRIMARY KEY(`userid`)