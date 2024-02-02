$("form[name=signup_form]").submit(function(e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/budget"
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault(); // Corrected this line
});

$("form[name=signin_form]").submit(function(e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signin",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard"
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault(); // Corrected this line
});

$("form[name=budget_form]").submit(function(e) {
    e.preventDefault();

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/budgeting",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard";
        },
        error: function(resp) {
            console.log(resp);

            // Check if resp.responseJSON is defined
            if (resp.responseJSON && resp.responseJSON.error) {
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            } else {
                $error.text("An unexpected error occurred.").removeClass("error--hidden");
            }
        }
    });
});

$("form[name=income_form]").submit(function(e) {
    e.preventDefault();

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/income",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard";
        },
        error: function(resp) {
            console.log(resp);

            // Check if resp.responseJSON is defined
            if (resp.responseJSON && resp.responseJSON.error) {
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            } else {
                $error.text("An unexpected error occurred.").removeClass("error--hidden");
            }
        }
    });
});
$("form[name=outcome_form]").submit(function(e) {
    e.preventDefault();

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/outcome",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard";
        },
        error: function(resp) {
            console.log(resp);

            // Check if resp.responseJSON is defined
            if (resp.responseJSON && resp.responseJSON.error) {
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            } else {
                $error.text("An unexpected error occurred.").removeClass("error--hidden");
            }
        }
    });
});
