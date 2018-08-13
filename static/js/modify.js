/**
 * Created by admin on 2017/12/11.
 */

function checkaction(v){
    if(v==0){
        var x=document.forms["register"]["id"].value;
        if(x==null || x==""){
            alert("修改内容为空，请点击返回重新选择");
            return false;
        }else{
            document.register.action="../modify/";
        }
    }else{
        document.register.action="../list/";
    }
    register.submit();
}
