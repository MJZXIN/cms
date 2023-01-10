package com.mxx.cms_api;

import com.mxx.cms_api.domain.User;
import com.mxx.cms_api.service.Impl.UserServiceImpl;
import com.mxx.cms_api.service.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class CmsApiApplicationTests {

    @Autowired
    private UserServiceImpl userService;

    @Test
    void contextLoads() {

    }

}
