package com.mxx.cms_api.utils;

import lombok.Data;

@Data
public class R {

    private int code;
    private Object data;
    private String msg;

    public R(int code, Object data, String msg) {
        this.code = code;
        this.data = data;
        this.msg = msg;
    }

    public R(int code, String msg) {
        this.code = code;
        this.data = null;
        this.msg = msg;
    }

    public R(int code, Object data) {
        this.code = code;
        this.data = data;
        this.msg = "";
    }

    public R(String msg) {
        this.code = 0;
        this.data = null;
        this.msg = msg;
    }
    public R() {
        this.code = 0;
        this.data = null;
        this.msg = "服务器异常";
    }
}
