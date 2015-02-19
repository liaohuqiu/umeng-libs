## 资源

将资源打包成aar包，aar包已经发布到中央库，在maven中引入:

```
<dependency>
    <groupId>in.srain.mix</groupId>
    <artifactId>umeng-share</artifactId>
    <version>{latest_version}</version>
    <type>aar</type>
</dependency>
```

在gradle中:

```
compile 'in.srain.mix:umeng-share:{latest_version}'
```

## 依赖库

各个依赖的jar包，通过mavn方式引入:

### For maven

maven库地址:

```
<repository>
    <id>github-srain-umeng-lib</id>
    <url>https://raw.githubusercontent.com/liaohuqiu/umeng-share/master/mvn-dependencies/repository</url>
    <releases>
        <enabled>true</enabled>
    </releases>
    <snapshots>
        <enabled>true</enabled>
    </snapshots>
</repository>
```

各个依赖组件:

```

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_WeiXin_1</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_facebook_1</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>umeng_social_sdk</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_sms</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_QQZone_2</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_QQZone_1</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_WeiXin_2</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_facebook_2</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_Sina</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_email</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>SocialSDK_QQZone_3</artifactId>
    <version>1.0.1</version>
    <type>jar</version>
</dependency>

<dependency>
    <groupId>com.umeng</groupId>
    <artifactId>umeng-analytics</artifactId>
    <version>5.4.1</version>
    <type>jar</version>
</dependency>

```

### For gradle

依赖库地址:

```
maven {
    url 'https://raw.githubusercontent.com/liaohuqiu/umeng-share/master/mvn-dependencies/repository'
}
```

各个依赖组件:

```
compile 'com.umeng:SocialSDK_WeiXin_1:1.0.1@jar'
compile 'com.umeng:SocialSDK_facebook_1:1.0.1@jar'
compile 'com.umeng:umeng_social_sdk:1.0.1@jar'
compile 'com.umeng:SocialSDK_sms:1.0.1@jar'
compile 'com.umeng:SocialSDK_QQZone_2:1.0.1@jar'
compile 'com.umeng:SocialSDK_QQZone_1:1.0.1@jar'
compile 'com.umeng:SocialSDK_WeiXin_2:1.0.1@jar'
compile 'com.umeng:SocialSDK_facebook_2:1.0.1@jar'
compile 'com.umeng:SocialSDK_Sina:1.0.1@jar'
compile 'com.umeng:SocialSDK_email:1.0.1@jar'
compile 'com.umeng:SocialSDK_QQZone_3:1.0.1@jar'
compile 'com.umeng:umeng-analytics:5.4.1@jar'

```
