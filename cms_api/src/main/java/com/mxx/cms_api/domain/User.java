package com.mxx.cms_api.domain;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import lombok.Data;

import java.time.LocalDateTime;

@Data
public class User {

    @TableId(type = IdType.ASSIGN_ID)
    private Long user_id;
    private String username;
    private String password;
    private String user_type;
    private String nick_name;
    private LocalDateTime create_date;
    private LocalDateTime update_date;
    private String create_by;
    private String login_ip;
    private String login_date;
    private String status;
    private String remark;
    private String update_by;
    private String email;
    private String phone;
    private String sex;
    private String del_flag;
    private String avatar;

}
