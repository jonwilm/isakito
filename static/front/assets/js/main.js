$(window).ready(function() {
  changeSizeNavbar();
})
$(window).scroll(function() {
  changeSizeNavbar();
});
$(window).resize(function() {
  changeSizeNavbar();
});
function changeSizeNavbar() {
  if ($(window).scrollTop() > 100) {
    $(".logo-navbar").css("height", "50px");
    if ($(window).width() > 992) {
      $(".pre-nav").css({"opacity": "0", "pointer-events": "none"});
      $(".navbar-nav").css("transform", "translateY(-65%)");
    }
  } else {
    $(".logo-navbar").css("height", "70px");
    if ($(window).width() > 992) {
      $(".pre-nav").css({"opacity": "1", "pointer-events": "all"});
      $(".navbar-nav").css("transform", "translateY(0)");
    }
  }
}