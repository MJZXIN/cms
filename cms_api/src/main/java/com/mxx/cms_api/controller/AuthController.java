package com.mxx.cms_api.controller;

import com.mxx.cms_api.utils.R;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("")
public class AuthController {

    @GetMapping("login")
    public R login() {
        log.warn("有用户请求登录");
        return new R(200, "登录成功");
    }
}
