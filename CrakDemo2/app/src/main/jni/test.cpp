//
// Created by cff on 2020/6/28.
//

#include "com_example_crakdemo2_MyJni.h"

JNIEXPORT jboolean JNICALL Java_com_example_crakdemo2_MyJni_isOk(JNIEnv *env, jclass obj, jstring para){

    int length = (env)->GetStringLength(para);
    if(length > 10){

        return true;
    }

    return false;
}