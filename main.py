import flet as ft

from database import init_db

from views.home_view import home_view
from views.classes_view import classes_view
from views.students_view import students_view
from views.attendance_view import attendance_view
from views.statistics_view import statistics_view
from views.reports_view import reports_view
from views.users_view import users_view


def main(page: ft.Page):

    init_db()

    page.title = "SmartAttendance"

    page.rtl = True

    page.window_width = 1000
    page.window_height = 700

    page.scroll = ft.ScrollMode.AUTO

    content = ft.Container(
        expand=True
    )

    def refresh_view(view):

        content.content = view

        page.update()

    # ==========================
    # الرئيسية
    # ==========================

    def open_home(e=None):

        refresh_view(
            home_view(
                open_classes,
                open_students,
                open_attendance,
                open_statistics,
                open_reports,
                open_users
            )
        )

    # ==========================
    # الصفوف
    # ==========================

    def open_classes(e=None):

        refresh_view(
            classes_view(
                page,
                open_home
            )
        )

    # ==========================
    # الطلاب
    # ==========================

    def open_students(e=None):

        refresh_view(
            students_view(
                page,
                open_home
            )
        )

    # ==========================
    # التحضير
    # ==========================

    def open_attendance(e=None):

        refresh_view(
            attendance_view(
                page,
                open_home
            )
        )

    # ==========================
    # الإحصائيات
    # ==========================

    def open_statistics(e=None):

        refresh_view(
            statistics_view(
                page,
                open_home
            )
        )

    # ==========================
    # التقارير
    # ==========================

    def open_reports(e=None):

        refresh_view(
            reports_view(
                page,
                open_home
            )
        )

    # ==========================
    # المستخدمون
    # ==========================

    def open_users(e=None):

        refresh_view(
            users_view(
                page,
                open_home
            )
        )

    # إضافة الحاوية للصفحة
    page.add(content)

    # فتح الشاشة الرئيسية
    open_home()


ft.app(target=main)
