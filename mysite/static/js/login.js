/**
 * Created by python on 17-1-5.
 */
$(function () {
   var error_name = false;
   var error_password = false;

   	$('#username').blur(function() {
		check_username();
	});

	$('#userpwd').blur(function() {
		check_userpwd();
	});



    function check_username() {
		var username = $('#username').val();
        var len = username.length;
        var re =/^[A-Za-z0-9_]{6,18}$/;

        if (len == 0) {
            $('#username').next().html('请输入用户名');
            $('#username').next().show();
            error_name = true;
        }
        else {
            if (re.test($('#username').val())) {
                $('#username').next().hide();
                error_name = false;
            }
            else {
                $('#username').next().html('请输入正确的用户名');
                $('#username').next().show();
                error_name = true;
            }
        }
    }

    function check_userpwd() {
        var userpwd =$('#userpwd').val();
        var len = userpwd.length;
        var re = /^[A-Za-z0-9_]{6,18}$/;
        var username = $('#username').val();

        if (len == 0) {
            $('#userpwd').next().html('请输入密码');
            $('#userpwd').next().show();
            error_password = true;
        }
        else {
            if (re.test($('#userpwd').val())) {
                $('#userpwd').next().hide();
                error_password = false;
            }

            else {
                $('#userpwd').next().html('您输入的密码格式不正确');
                $('#userpwd').next().show();
                error_password = true;
            }
        }
    }




	$('#input_info').submit(function() {
		check_username();
		check_userpwd();
		if(error_name == false && error_password == false )
		{
            return true;
		}
		else {
		    return false;
        }

	});
});