     $(document).ready(function () {
            $(window).keydown(function (event) {
                if (event.keyCode == 13) {
                    event.preventDefault();
                    return false;
                }
            });
        });

        $(document).on("keydown", "form", function (event) {

            var key = event.which;
            switch (key) {
                case 13: // enter
                    var text_search = $("#hadith-search").val();
                    make_request(text_search)
                    console.log(text_search);

                    break;
                default:
                    break;
            }

        });
        //  document.getElementById("hadith-search").disabled = true;
        var result_arae = $(".result-items-area");



        function append_new_data(hadith_data){
         var hadith_list = []

         for (let index = 0; index < hadith_data['hits']['hits'].length; index++) {
            hadith_item = hadith_data['hits']['hits'][index]['_source'];

            hadith_list.push(
                `
                <div class="hadith-item">
                <div class="hadith">
                    <p> ${hadith_item['arabic_hadith']}</p>
                </div>
                <div class="hadith-info">
                    <div class="info">
                        <p class="data-desc">كتاب :</p>
                        <p class="data-value">${hadith_item['chapter_arabic']}</p>
                        <p>${hadith_item['chapter_number']}</p>
                    </div>
                    <div class="info">
                        <p class="data-desc">باب :</p>
                        <p class="data-value">${hadith_item['section_arabic']}</p>
                        <p>${hadith_item['section_number']}</p>
                    </div>
                    <div class="info">
                        <p class="data-desc">النوع :</p>
                        <p class="data-value">${hadith_item['arabic_grade']}</p>
                    </div>
                </div>
            </div>
                `
            )

        }

        result_arae.append(hadith_list);
        }


        function make_request(text_query) {
            result_arae.empty();
             var data ={"query":text_query};
//            var data = '{"query":"'+text_query+'"}';
//            data["query"]=text_query;
             $.ajax({
                 type: "POST",
                 url: "http://127.0.0.1:8000/api/search/",
                 data: JSON.stringify(data),
                 contentType: "application/json; charset=utf-8",
                 dataType: "json",
                 success: function (json) {
                     append_new_data(json);
                     // do stuff with json (in this case an array)
//                     alert("Success");
                 },
                 error: function (error) {
                 console.log("error");
                     console.log(error);
                 }
             });


        }
