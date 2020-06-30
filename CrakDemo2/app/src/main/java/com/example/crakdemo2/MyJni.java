package com.example.crakdemo2;

public class MyJni {

    static {

        System.loadLibrary("MyJni");
    }

    public native static boolean isOk(String para);
}
