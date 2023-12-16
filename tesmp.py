
following_locator = page.locator('body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1)')
followingUsersElements = following_locator.locator('.x1a02dak.x1q0g3np.xdl72j9 a[role="link"]')

for followingUsersElement in followingUsersElements {
    userName = followingUsersElement.innerText()
    print(userName)
}
followingUserNames = []
console.log(followingUserNames)