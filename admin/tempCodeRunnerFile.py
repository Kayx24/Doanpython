    selected_accounts = self.get_selected_accounts()
        if selected_accounts:
            self.delete_non_vip_accounts(selected_accounts)
        else:
            print("Không có tài khoản nào được chọn.")