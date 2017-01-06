$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{

		}
		else
		{

		}
	});


	function check_user_name() {
		var user_name = $('#user_name').val();
        var len = $('#user_name').val().length;
        var re =/^[A-Za-z0-9_]{6,18}$/;
        var date = {'uname':user_name}

        if (len == 0) {
            $('#user_name').next().html('请输入用户名');
            $('#user_name').next().show();
            error_name = true;
        }
        else {
            if (re.test($('#user_name').val())) {
            	$.post('/user_info/uname_verify/',date,function (dic) {
					if (dic.num == 0){
						$('#user_name').next().hide();
						error_name = false;
					}
					else{
						$('#user_name').next().html('用户名已拥有');
            			$('#user_name').next().show();
            			error_name = true;
					}
				});
            }
            else {
                $('#user_name').next().html('您输入的用户名格式不正确');
                $('#user_name').next().show();
                error_name = true;
            }
        }
    }

	function check_pwd() {
        var len = $('#pwd').val().length;
        var re = /^[A-Za-z0-9_]{6,18}$/;
        if (len == 0) {
            $('#pwd').next().html('请输入密码');
            $('#pwd').next().show();
            error_password = true;
        }
        else {
            if (re.test($('#pwd').val())) {
                $('#pwd').next().hide();
                error_password = false;
            }

            else {
                $('#pwd').next().html('您输入的密码格式不正确');
                $('#pwd').next().show();
                error_password = true;
            }
        }
    }

	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}
	// /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/
	function check_email() {
        var re = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
        var len = $('#email').val().length;
        if (len == 0) {
            $('#email').next().html('请输入您的邮箱');
            $('#email').next().show();
            error_check_password = true;
        }
        else {
            if (re.test($('#email').val())) {
                $('#email').next().hide();
                error_email = false;
            }
            else {
                $('#email').next().html('你输入的邮箱格式不正确');
                $('#email').next().show();
                error_check_password = true;
            }
        }
    }


	$('#infomation').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			alert('注册成功');
			return true;
		}
		else
		{
			return false;
		}

	});





})