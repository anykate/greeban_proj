$("form.form_prod").on("submit", function (e) {
  var that = $(this),
    url = that.attr("action"),
    type = that.attr("method"),
    data = {};

  that.find("[name]").each(function (index, value) {
    var that = $(this),
      name = that.attr("name"),
      value = that.val();
    data[name] = value;
  });
  $.ajax({
    url: url,
    type: type,
    data: data,
    success: function (response) {
      prod_id = "#prod_" + response.product_id;
      $(prod_id).html(response.cart[response.product_id]);
    },
  });
  return false;
});
