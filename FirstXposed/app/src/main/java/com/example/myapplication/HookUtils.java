package com.example.myapplication;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public class HookUtils implements IXposedHookLoadPackage {

    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam loadPackageParam) throws Throwable {

        if(loadPackageParam.packageName.equals("hfdcxy.com.myapplication")){

            XposedBridge.log("here");
            XposedHelpers.findAndHookMethod(loadPackageParam.classLoader.loadClass("hfdcxy.com.myapplication.MainActivity"),
                    "check",
                    String.class,
                    String.class,
                    new XC_MethodHook() {

                        @Override
                        protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                            super.beforeHookedMethod(param);

                            XposedBridge.log("------------beforeHookedMethod start------------");
                            String userName = (String)param.args[0];
                            String password = (String)param.args[1];
                            XposedBridge.log("userName:" + userName + ",password:" + password);
                            XposedBridge.log("------------beforeHookedMethod end------------");
                        }

                        @Override
                        protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                            super.afterHookedMethod(param);

                            XposedBridge.log("------------afterHookedMethod start------------");
                            String userName = (String)param.args[0];
                            String password = (String)param.args[1];
                            XposedBridge.log("userName:" + userName + ",password:" + password);
                            XposedBridge.log("------------afterHookedMethod end------------");
                        }
                    });

        }
    }
}
