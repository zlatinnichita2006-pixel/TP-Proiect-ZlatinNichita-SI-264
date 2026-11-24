from arsenal.windows.inventar import Eveniment, Inventar, Proces

# B4

def test_proces_din_temp_e_suspect():
    p = Proces(1, "x.exe", "ana", "C:\\Users\\ana\\AppData\\Local\\Temp\\x.exe")
    assert p.e_suspect() is True


def test_proces_din_windows_nu_e_suspect():
    p = Proces(2, "svchost.exe", "SYSTEM", "C:\\Windows\\System32\\svchost.exe")
    assert p.e_suspect() is False


def test_proces_egalitate_dataclass():
    p1 = Proces(3890, "svch0st.exe", "ana", r"C:\Users\ana\AppData\Roaming\svch0st.exe")
    p2 = Proces(3890, "svch0st.exe", "ana", "C:\\Users\\ana\\AppData\\Roaming\\svch0st.exe")
    assert p1 == p2
    assert p1.e_suspect() is True


def test_eveniment_e_suspect():
    ev_id = Eveniment(4625, "warning", "Security", "administrator", "Failed logon")
    ev_crit = Eveniment(9001, "critical", "System", "SYSTEM", "Critical error")
    ev_normal = Eveniment(4624, "information", "Security", "ana", "Successful logon")

    assert ev_id.e_suspect() is True
    assert ev_crit.e_suspect() is True
    assert ev_normal.e_suspect() is False


def test_inventar_metode():
    inv = Inventar([
        Proces(10, "svchost.exe", "SYSTEM", r"C:\Windows\System32\svchost.exe"),
        Proces(20, "update.exe", "ana", r"C:\Users\ana\AppData\Local\Temp\update.exe"),
    ])
    assert len(inv) == 2
    assert len(inv.suspecte()) == 1
    assert inv.pe_user() == {"SYSTEM": ["svchost.exe"], "ana": ["update.exe"]}