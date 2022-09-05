package com.mxx.cms_api.service.Impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mxx.cms_api.domain.User;
import com.mxx.cms_api.mapper.UserMapper;
import com.mxx.cms_api.service.UserService;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {
}
