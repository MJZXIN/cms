package com.mxx.cms_api.component;

import com.alibaba.fastjson2.JSONObject;
import com.mxx.cms_api.utils.R;
import lombok.extern.slf4j.Slf4j;
import netscape.javascript.JSObject;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.logout.LogoutSuccessHandler;
import org.springframework.stereotype.Component;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Slf4j
@Component
public class custLogoutSuccessHandler implements LogoutSuccessHandler {

    @Override
    public void onLogoutSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        log.warn(authentication.getName() + "--用户退出");
        response.setContentType("application/json;charset=utf-8");
        response.getWriter().write(JSONObject.toJSONString(new R(200,"用户退出成功")));
    }
}
