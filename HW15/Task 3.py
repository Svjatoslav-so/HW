from functools import reduce


# Task 3
class ReportInLineDecorator:
    def __init__(self, func):
        self.func = func

    # представляет отчет в виде одной строки
    def __call__(self, *args, **kwargs):
        report = self.func(*args, **kwargs)
        report_items = report.split("\n")
        report = reduce(lambda x, y: x + " " + y.capitalize(), report_items, "")
        return report


class ReportInTableDecorator:
    def __init__(self, func, cell_width=20):
        self.func = func
        # ширина ячейки таблицы
        self.cell_width = cell_width

    # представляет отчет в виде таблицы
    def __call__(self, *args, **kwargs):
        report = self.func(*args, **kwargs)

        table = list(map(lambda x: x.split(":"), report.split("\n")))

        # разбиваем строку каждой ячейки, на список строк длиной не больше ширины ячейки
        header_row_list = self.__fit_in_column_width([i[0].capitalize() for i in table])
        value_row_list = self.__fit_in_column_width([i[1] for i in table])

        # собираем полученный список списков в строку
        header_row = self.__convert_to_row(header_row_list)
        value_row = self.__convert_to_row(value_row_list)

        # составляем строки-горизонтальные-границы таблицы
        column_num = len(table)
        table_width = column_num * (self.cell_width + 1)
        horiz_line = self.__draw_hline(table_width)
        horiz_line2 = self.__draw_hline(table_width, "-")

        # собираем все полученные строки в одну строку
        report = horiz_line + header_row + horiz_line2 + value_row + horiz_line
        return report

    # принимает список строк(каждая строка - значение ячейки)
    # разбивает каждую строку на список строк длиной не больше ширины ячейки
    # возвращает список списков строк
    def __fit_in_column_width(self, cell_list):
        result_list = [[""] for i in range(len(cell_list))]
        for i in range(len(cell_list)):
            words = cell_list[i].split()
            for w in words:
                if len(result_list[i][len(result_list[i]) - 1]) + len(w) < self.cell_width:
                    result_list[i][len(result_list[i]) - 1] += w + " "
                else:
                    result_list[i].append(w + " ")
        return result_list

    # принимает список списков строк, который возвращает __fit_in_column_width
    # превращает его в единую строку, которая при выводе представляет строку таблицы
    def __convert_to_row(self, cell_list):
        max_num_of_lines_in_cell = max([len(v) for v in cell_list])
        row = ""
        for k_line in range(max_num_of_lines_in_cell):
            for column in range(len(cell_list)):
                if k_line < len(cell_list[column]):
                    row += f"|{cell_list[column][k_line]:^{self.cell_width}}"
                else:
                    row += f"|{'':^{self.cell_width}}"
            row += "|\n"
        return row

    # возвращает строку длинной length, составленную из symbol
    @staticmethod
    def __draw_hline(length, symbol="_"):
        return symbol * length + "\n"


# @ReportInLineDecorator
# @ReportInTableDecorator
def get_report():
    return """выручка: 12 000 000 грн.
закупочная стоимость товара: 6 000 000 грн.
коммерческие расходы: 1 500 000 грн.
проценты к уплате: 500 000 грн.
текущий налог на прибыль: 600 000 грн."""


table_report = ReportInTableDecorator(get_report, 25)
inline_report = ReportInLineDecorator(get_report)

print(get_report())
print(inline_report())
print(table_report())
